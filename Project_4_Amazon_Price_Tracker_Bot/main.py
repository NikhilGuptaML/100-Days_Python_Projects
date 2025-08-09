import smtplib
from httpx import ConnectTimeout
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import json
load_dotenv()

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")
header=json.loads(os.getenv("header"))
amazon_link=os.getenv("amazon_link")
def send_mail(current_price):
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        try:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:The selected item price has drop\n\nThe item you wanted had a price drop and is currently @ {current_price}")
        except Exception as e:
            raise RuntimeError(f"Failed to send {e}")
        else:
            print("Email was sent successfully.")

def request_price():
    try:
        response=requests.get(amazon_link,headers=header,timeout=10)
    except ConnectTimeout:
        raise BufferError("Connection Timedout... Try Again...")
        
    content=BeautifulSoup(response.text,features='html.parser')

    price=content.find('span',class_='a-price-whole')
    if not price:
        raise ValueError("Price element not found. Amazon page structure may have changed.")

    return price.text

def main():
    current_price=request_price()
    
    if(int(current_price.replace(",","").strip("."))<160000):
        send_mail(current_price)

if __name__=="__main__":
    main()




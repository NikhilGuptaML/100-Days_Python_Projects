import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "RELIANCE.BSE"
COMPANY_NAME ="RELIANCE"

#----------------------------------API KEY-------------------------------------------#
API_KEY_STOCK=os.getenv("API_KEY_STOCK")

API_KEY_NEWS=os.getenv("API_KEY_NEWS")

#----------------------------------SETTING UP TWILIO---------------------------------#
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
AUTH_SID=os.getenv("account_sid")
INCOMING_NO=os.getenv('INCOMING_NO')
OUTGOING_NO=os.getenv('OUTGOING_NO')

account_sid = AUTH_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

message_sid=os.getenv('Messaging_Service_SID')

#------------------------------------Getting Stock Information-------------------------#
parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":API_KEY_STOCK
}

request=requests.get("https://www.alphavantage.co/query",params=parameters)
request.raise_for_status()
data=request.json()

stock_name=data["Meta Data"]["2. Symbol"]
stock=data["Time Series (Daily)"]
stockprice_of_day_before=list(stock.items())[0]
stock_open=float(stockprice_of_day_before[1]["1. open"])
stock_close=float(stockprice_of_day_before[1]["4. close"])

difference_in_price=stock_close-stock_open

#---------------------------------Getting News about the stock-------------------------#
parameter={
    "qInTitle":COMPANY_NAME,
    "from":list(stock.items())[1][0],
    "to":stockprice_of_day_before[0],
    "sortBy":"popularity",
    "apiKey":API_KEY_NEWS
    }

if abs(difference_in_price)>(0.02*stock_open):
    request_news=requests.get("https://newsapi.org/v2/everything",params=parameter)
    request_news.raise_for_status()
    articles=request_news.json()["articles"]
    title=""
    if difference_in_price>0:
        title+=f"{COMPANY_NAME} 🔺\n"
    else:
        title+=f"{COMPANY_NAME} 🔻\n"

    
    for i in range(min(2, len(articles))):
        message=""
        message+=f'Title: {articles[i]["title"]}\n'
        message+=f'Description: {articles[i]["description"]}'

        finalmsg=title+message
        #-------------------------Sending SMS-----------------------------------#
        generate_message = client.messages.create(
            messaging_service_sid=message_sid,
            body=finalmsg,
            from_ =INCOMING_NO,
            to=OUTGOING_NO
        )


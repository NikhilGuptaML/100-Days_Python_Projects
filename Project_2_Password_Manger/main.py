
from tkinter import messagebox
from password import create_password
import pyperclip
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password=create_password()
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if not website or not email or not password:
        messagebox.showerror(title="Error",message="Feild cannot be empty")
        return
    is_ok=messagebox.askokcancel(title=website,message="These are the credeentials you have entered:\n" \
    f"Email:{email}\n" \
    f"Password:{password}")
    
    if is_ok:
        new_data={
            website:{
                    "Email":email,
                    "Password":password
            }
        }
        try:
            with open(file_path,"r") as f:
                data=json.load(f)
                
        except (json.decoder.JSONDecodeError,FileNotFoundError):
            data={}

        data.update(new_data)

        with open(file_path,"w") as f:
            json.dump(data,f,indent=4)
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            email_entry.insert(0,"YOUR EMAIL HERE")
            password_entry.delete(0,END)
# ---------------------------- SEARCH  ------------------------------- #
def search():
    website=website_entry.get()
    try:
        with open(file_path,"r") as f:
            data=json.load(f)
    except (json.decoder.JSONDecodeError,FileNotFoundError):
        messagebox.showerror(title="Error",message="No Data Found")
    finally:
        if website in data:
            messagebox.showinfo(title=website,message=f"Email: {data[website]['Email']}\nPassword:  {data[website]['Password']}")
        else:
            messagebox.showerror(title="Error",message="Data not found")
            

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import * # type: ignore

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
photoimage=PhotoImage(file="Project_2_Password_Manger\logo.png")
canvas.create_image(100,100,image=photoimage)
canvas.grid(row=0,column=1)

#Label

website_label=Label(text="Website")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)

password_label=Label(text="Password")
password_label.grid(row=3,column=0)

#Input Boxes
website_entry=Entry(width=32)
website_entry.grid(row=1,column=1,columnspan=2,sticky='W')
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky='EW')
email_entry.insert(0,"YOUR EMAIL HERE")

password_entry=Entry(width=32)
password_entry.grid(row=3,column=1,sticky="W")

#Button
password_button=Button(text="Create Password",command=generate_password,highlightthickness=0)
password_button.grid(row=3,column=2,sticky="EW")

add_button=Button(text="Add",width=36,command=save,highlightthickness=0)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")

search_button=Button(text="Search",highlightthickness=0,command=search)
search_button.grid(row=1,column=2,sticky="EW")


window.mainloop()
#
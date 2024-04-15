from tkinter import*
from tkinter import messagebox
import os
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def PasswordGenerator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    PasswordEntry.delete(0,END)

    password_list = [random.choice(letters) for newLetter in range(nr_letters)] + [random.choice(symbols) for newSymbol in range(nr_symbols)] + [random.choice(numbers) for newNumber in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    PasswordEntry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def SavePasswordInTXTFile():

    Website = WebsiteEntry.get()
    Email = EmailUserNameEntry.get()
    Password = PasswordEntry.get()

    DATA = {
        Website: {
            "Email": Email,
            "Password": Password,
            
        }
    }

    if len(Website)>1 and len(Email)>1 and len(Password)>1:

        is_ok = messagebox.askokcancel(title=Website,message=f"These are the details entered: \nEmail: {Email} \nPassword: {Password} \nAre you Okay with that?")

        try:
            with open("data.json","r" ) as data_file:
                #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(DATA)
        except FileNotFoundError: 
            with open("data.json", "w") as data_file:
                json.dump(DATA,data_file,indent=4)
        else:
            with open("data.json", "w") as data_file:
                #saving the Update 
                json.dump(data,data_file,indent=4)
        finally:
            WebsiteEntry.delete(0,END)
            PasswordEntry.delete(0,END)
    else:
         messagebox.showerror(title="oops",message="Please dont leave any fields empty!")
             


def find_password():
    
    try:
        Website = WebsiteEntry.get()
        with open("data.json","r" ) as data_file:
            #Reading old data
            data = json.load(data_file)
            email = data[Website]["Email"]
            password = data[Website]["Password"]

    except KeyError:
        messagebox.showerror(title="WEBSITE NOT FOUND", message=f"ERROR!!\nThe Website {Website} was not found!")
    except FileNotFoundError:
        messagebox.showerror(title="FILE NOT FOUND", message="ERROR!!\nThe File was not found!")
    else:
        messagebox.showinfo(title=Website,message=f"Email: {email}\nPassword: {password}")
    finally:
        WebsiteEntry.delete(0,END)
        PasswordEntry.delete(0,END)
        
                
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=50,pady=50)



canvas = Canvas(width=200,height=200)
myPassPic = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = myPassPic)
canvas.grid(row=0,column=1)

WebsiteLabel = Label(text="Website: ")
WebsiteLabel.grid(row=1,column=0)

WebsiteEntry = Entry(width=34)
WebsiteEntry.focus()
WebsiteEntry.grid(row=1,column=1)

EmailUserNameLabel = Label(text="Email/Username: ")
EmailUserNameLabel.grid(row=2,column=0)

EmailUserNameEntry = Entry(width=53)
EmailUserNameEntry.insert(END,"abdelilahkjaarani@yahoo.com")
EmailUserNameEntry.grid(row=2,column=1,columnspan=2)

PasswordLabel = Label(text="Password: ")
PasswordLabel.grid(row=3,column=0)

PasswordEntry = Entry(width= 34)
PasswordEntry.grid(row=3, column=1)

GeneratePsswrdBttn = Button(text="Generate Password",width=14,command=PasswordGenerator)
GeneratePsswrdBttn.grid(row=3,column=2)

AddButton = Button(text="Add", width=44, command=SavePasswordInTXTFile)
AddButton.grid(row=4,column=1,columnspan=2)

SearchButton = Button(text="Search",width=14,command=find_password)
SearchButton.grid(row=1,column=2)





















window.mainloop()
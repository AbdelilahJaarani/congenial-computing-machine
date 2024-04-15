import smtplib
import datetime as dt
import random

#Normale Email Adresse 
my_mail = "juubijaarani@gmail.com"
pw = "zvwcdbpogdbzxmkm"

#The Provider which has to be connected



with open("quotes.txt") as qoute_file:
    all_qoute = qoute_file.readlines()
    rdnQoute = random.choice(all_qoute)






now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4: 
    with smtplib.SMTP("smtp.gmail.com") as connection:
    #Makes the connection secure
        connection.starttls()
        connection.login(user=my_mail, password=pw)
        connection.sendmail(from_addr=my_mail, 
                        to_addrs="abdelilahjaarani@gmail.com",
                        msg="Subject:MOTIVATION FRIDAY\n\n"f"{rdnQoute}")



print(weekday)
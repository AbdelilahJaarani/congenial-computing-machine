import requests
import smtplib
from datetime import datetime 


class SunriseAndSunset:
    def __init__(self):
        self.MyLat = 50.133881
        self.MyLong = 8.527120
        self.MyParameter = {
            "lat": self.MyLat,
            "lng": self.MyLong,
            "formatted": "0",
        }
    
    def myLat (self):
        return self.MyLat
    
    def myLong(self):
        return self.MyLong
        
    def getJsonData(self, api = "https://api.sunrise-sunset.org/json" ) :
        data = requests.get(api,params=self.MyParameter).json()
        return data
    
    def SunsetHour(self):
        sunsetHour = int(self.getJsonData()["results"]["sunset"].split("T")[1].split(":")[0])
        return sunsetHour
    
    def SunriseHour(self):
        sunriseHour = int(self.getJsonData()["results"]["sunrise"].split("T")[1].split(":")[0])
        return sunriseHour
    


class IssTracker(SunriseAndSunset):
    def __init__(self) -> None:
        super().__init__()
        self.issData = self.getJsonData(api="http://api.open-notify.org/iss-now.json")
        self.issPosLatitude = float (self.issData["iss_position"]["latitude"])
        self.issPosLongitude = float (self.issData["iss_position"]["longitude"])

    def IssUpOnCurrentCity(self):
        if (self.issPosLatitude <= self.MyLat + 5 and self.issPosLatitude >= self.MyLat -5) and (self.issPosLongitude <= self.MyLong + 5 and self.issPosLongitude >= self.MyLong -5) :
            print("ISS is on your current position!")
            return True
        else:
            print("ISS is NOT on your current position! Try it later...")
            return False
        

class Mail:
    def __init__(self) -> None:
        self.email = "abdelilahjaarani@gmail.com"
        self.password = "rtxckonfkdfoufdi"
        
    def SendingMail(self, subject, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.email,self.password)
            connection.sendmail(from_addr=self.email, to_addrs=self.email, 
                            msg= f"Subject: {subject} \n\n {message}")
        successReport = "Sending Message was successfull! "
        return successReport

    
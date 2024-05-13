from cons import SunriseAndSunset 
from cons import IssTracker
from cons import Mail 

ss = SunriseAndSunset()
iss = IssTracker()
mail = Mail()

currentSunsetHour = ss.SunsetHour()
currentSunriseHour = ss.SunriseHour()

currenLatitude = ss.myLat()
currenLongitude = ss.myLong()

if not iss.IssUpOnCurrentCity():
    msg = "The ISS is not on your current position"
    mail.SendingMail(subject="ISS NOT YOUR DESTINATION", message= msg)
else:
    msg = "Look UP! The ISS is there"
    mail.SendingMail(subject="Look Up!", message= msg) 
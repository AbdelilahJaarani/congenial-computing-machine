import requests

MyLat = 50.133881
MyLong = 8.527120




MyParamenter = {
    "lat": MyLat,
    "lng": MyLong,
    "tzid": 1
}

response = requests.get("https://api.sunrise-sunset.org/json", params= MyParamenter)
data = response.json()
sunrise = data["results"]["sunrise"]
print(sunrise)
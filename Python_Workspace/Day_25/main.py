

#with open("weather_data.csv","r") as data_file:
   #data = data_file.readlines()
   
#print(data)

import csv

#with open ("weather_data.csv") as data_file:
   # data = csv.reader(data_file)
   # temperatur = []
   # for row in data:
        #if data.line_num >= 2:
            #temperatur.append(int(row[1]))
   # print(temperatur)

import pandas as pd

#temp = pd.read_csv("weather_data.csv")
#zahlen = temp["temp"].to_list()

#sum = 0
#for day in range (len(zahlen)):
   # sum += zahlen[day]
#average = sum / len(zahlen)
#dee = sum(zahlen) / len(zahlen)

#print (dee)
#max = temp["temp"].max()
#print(temp [temp["temp"] == max])

#monday = temp[temp.day == "Monday"]
#print(monday.temp)

#celcius = int(monday.temp)
#fahrenheit = (celcius * 1.8 + 32)
#print(fahrenheit)

data = pd.read_csv("centralpark_squirl_data.csv")
gray_squirl = data[data["Primary Fur Color"] == "Gray"]
red_squirl = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirl = data[data["Primary Fur Color"] == "Black"]



color_count = {
    "Fur Color": ['grey','red','black'],
    "Count": [len(gray_squirl),len(red_squirl),len(black_squirl)]

}

newData = pd.DataFrame(color_count)
print(newData)
newData.to_csv("squirrel_count.csv")
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Streetcrossing Game")
player = Player()
score = Scoreboard()

carList = []

for car in range(15):
    car = CarManager()
    carList.append(car)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    #Turtle can move just Up and 
    player.move()

    #All cars are moving 
    for wheel in carList:
        #Hitting the Car
        if player.distance(wheel)>28:
         wheel.moving()
        else:
            score.game_over()
            game_is_on = False
                
         
        if wheel.xcor() < -325:
            wheel.goto(300,random.randint(-260,260))


    #The player arrived 
    if player.ycor()>280:
            player.refresh()
            score.new_lw()
                      
            for car in carList:
                car.increase_speed()

    



    #The player hit the Car
   
    screen.update()


screen.exitonclick()

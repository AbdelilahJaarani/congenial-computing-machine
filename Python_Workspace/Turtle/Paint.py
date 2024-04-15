from turtle import Turtle, Screen
import random
import colorgram

aj = Turtle()
screen = Screen()
screen.colormode(255)

num = 34
colors = colorgram.extract('Picture.JPG',num)

colorlist = []
for i in range (num):
    colotm = (colors[i].rgb.r,colors[i].rgb.g,colors[i].rgb.b)
    colorlist.append(colotm)


aj.speed(0)
aj.hideturtle()

def hirst_project(thickness,distance,amount,startX=0,startY=0):
    for i in range (amount):
        aj.penup()
        aj.goto(startX,(i*distance)-startY)

        for i in range (amount):
            aj.color(random.choice(colorlist))
            aj.dot(thickness)
            aj.penup()
            aj.fd(distance)


hirst_project(25,30,10)




screen.exitonclick()
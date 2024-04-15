from turtle import Turtle, Screen
import random


aj = Turtle()
screen = Screen()
screen.colormode(255)

color = ["medium aquamarine","orange red", "dark turquoise","cornflower blue", "magenta", "red", "yellow", "green", "dark slate blue", "blue"]

def random_color():
   r = random.randint(0,255)
   g = random.randint (0,255)
   b = random.randint (0,255)
   rgb = (r,g,b)
   return rgb



moving = [0,90,180,270]

aj.pensize(1)
aj.speed(0)

#gab sagt den Abstand aus von den muss als inter mit 360 geteilt werden damit er genau an dem Punkt aufhoert wo er gestartet hatte
def spiral (gab):  
    for i in range (int(360/gab)):
        aj.pencolor(random_color())
        aj.circle(100)
        aj.rt(gab)

    

spiral(5)




screen.exitonclick()


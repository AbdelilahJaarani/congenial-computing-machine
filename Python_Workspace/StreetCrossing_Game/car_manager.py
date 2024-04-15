from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = -10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid= 1.1, stretch_len= 2.2)
        self.color(random.choice(COLORS))
        self.goto(random.randint(-300,300),random.randint(-260,260))
        self.newX = STARTING_MOVE_DISTANCE
        



    def moving(self):
       newX = self.xcor() - self.newX
       self.goto(newX,self.ycor())
    
    def increase_speed(self):
        self.newX -=  MOVE_INCREMENT

    def refresh(self):
        self.newX = STARTING_MOVE_DISTANCE
       
    


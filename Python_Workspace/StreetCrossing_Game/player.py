from turtle import Turtle
from turtle import Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)
        self.newX = 0
        self.newY = 0

    
    
    def fd(self):
         self.newY = self.ycor() + MOVE_DISTANCE
         self.goto(self.newX,self.newY)

    def move(self):
        screen.onkey(self.fd, "Up")
        screen.listen()
    
    def refresh(self):
        self.goto(STARTING_POSITION)
        
       


        
        
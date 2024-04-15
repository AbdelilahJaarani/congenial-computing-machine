from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1,5)
        self.seth(-90)
    

    def pos(self,x,y):
        self.speed(0)
        self.penup()
        self.goto(x,y)

    def move_down(self):
        self.fd(20)
    
    def move_up(self):
        self.fd(-20)
    


from turtle import Turtle
from turtle import Screen

MOVING_DISTANCE = 20
START_POS = [(0,0), (-20,0), (40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) :
        self.snake = []
        self.newX = 0
        self.newY = 0
        self.screen = Screen()
        self.create_Turtle()
        self.head = self.snake[0]



    def create_Turtle(self):
        
        for position in START_POS:
            self.increase_snake(position)
       
            

    def increase_snake(self,position):
         i = Turtle("square")
         i.color("white")
         i.penup()
         i.goto(position)
         self.snake.append(i)

    def extend(self):
        self.increase_snake(self.snake[-1].pos())
       

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def reset(self):
        for snk in self.snake:
            snk.goto(1000,1000)
        self.snake.clear()
        self.create_Turtle()
        self.head = self.snake[0]
    

    def move(self):
            
        for square_nr in range(len(self.snake)-1,0,-1):
            self.newX = self.snake[square_nr-1].xcor()
            self.newY = self.snake[square_nr-1].ycor()
            self.snake[square_nr].goto(self.newX,self.newY)

        self.snake[0].fd(MOVING_DISTANCE)
        self.screen.onkey(self.turn_right,"d")
        self.screen.onkey(self.turn_left,"a")
        self.screen.onkey(self.turn_up,"w")
        self.screen.onkey(self.turn_down,"s")
        self.screen.listen()
    
    

        
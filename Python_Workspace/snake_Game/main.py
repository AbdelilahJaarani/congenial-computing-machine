from turtle import Screen
from turtle import Turtle
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def turning_snake(obj):
    obj.lt(90)
    

def get_snake(amount_start_square):
    snake = []
    for i in range (amount_start_square):
        i = Turtle("square")
        i.color("white")
        i.penup()
        i.speed(0)
        snake.append(i)
    for j in range(amount_start_square):
        snake[j].goto(j*(-20),0)
    return snake


def moving_snake(snake_list):
    moving = False
    while not moving:
        screen.update()
        time.sleep(0.1)

        for square_nr in range(len(snake_list)-1,0,-1):
            newX = snake_list[square_nr-1].xcor()
            newY = snake_list[square_nr-1].ycor()
            snake_list[square_nr].goto(newX,newY)

        snake_list[0].fd(20)
        screen.onkey(turning_snake(snake_list[0]),"up")
        screen.listen()
            
        
        
        
        

        


snake = get_snake(amount_start_square=3)
moving_snake(snake)







screen.exitonclick()
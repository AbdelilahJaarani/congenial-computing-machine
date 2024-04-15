from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    #print(snake.snake[2].pos())

    #Detect eating the Food 
    if snake.head.distance(food) < 15:
       food.refresh()
       score.get_food()
       snake.extend()
       
    
    #Wall detecting
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-290:
        score.update_Highscore()
        snake.reset()


    #Tail detection
   # if snake.head.pos() in snake.snake:
        #game_is_on = False
    snk = []
    for i in snake.snake[1:]:
        if snake.head.distance(i)<10:
            score.update_Highscore()
            snake.reset()

        




screen.exitonclick()
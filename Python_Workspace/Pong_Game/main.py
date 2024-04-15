from ball import Ball
from turtle import Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
score = Scoreboard()


screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG GAME")
screen.tracer(0)

paddle1.pos(350,0)
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle1.move_up, "Up")
screen.listen()



paddle2.pos(-350,0)
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down,"s")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    #Detecting the wall up and down
    ball.move()
    if ball.ycor() > 280 or ball.ycor() <-275:
        ball.bounce_y()
    
    #Detection the paddle and bounce 

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    #right paddle
    if ball.xcor() > 400:
        ball.refresh()
        score.increase_score_left()
        

    #left paddle
    if ball.xcor ()< -400:
        ball.refresh()
        score.increase_score_right()
        
   




screen.exitonclick()
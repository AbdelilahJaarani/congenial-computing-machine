from turtle import Turtle, Screen
import random



#brauche 5 Tutrle die selbst generiert werden ohne dass es einzeln erstelle

screen = Screen()
screen.setup(500,400)
color = ["red","green","blue","yellow","black","saddle brown"]


    

def create_turtle(col):     
    i = Turtle("turtle")
    i.color(col)
    return i



    
def set_turtle (num):
    turtle_list = []
    for i in range (num):
        turtle = create_turtle(color[i])
        turtle.penup()
        turtle.goto(-230,(-(400/10)*(i+1/num))+100)
        turtle_list.append(turtle)
    return turtle_list


def go_turtle(list_turtle,num):
    goal = False
    while not goal:
        for i in range (num):
            list_turtle[i].fd(random.randint(0,10))
            if list_turtle[i].xcor() >= 220:
                goal = True
                return list_turtle[i].pencolor()
        
            


corret_color = False
while not corret_color:
    user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
    if user_bet in color:
        corret_color = True
        obj_list = set_turtle(5)
        bet = go_turtle(obj_list,5) 
        if bet  == user_bet:
            print (f"Your {bet} Turtle wins!!!")
        else:
            print(f"AHH You Lose!! The {bet} Turtle got it! ")
        

    else:
        print("Invalid Input!")
    
        


    
screen.exitonclick()



import turtle 
import pandas as pd

SCORE = 0

screen = turtle.Screen()
screen.title("US Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


abde = turtle.Turtle()
abde.hideturtle()
abde.color("black")
abde.penup()
abde.speed(0)



us = pd.read_csv("50_states.csv")
statesList = us["state"].to_list()
theRight_state = []
#learn_file = []




game_is_on = True #repeat evertime the question still has 
while game_is_on:
    answer_state = screen.textinput(f" {SCORE} / {len(statesList)} Guess the State","What is one State name? ")
    
    if answer_state.title() == "Exit":


        learning_list = [state for state in statesList if state not in theRight_state]
        #for state in statesList:
           # if state not in theRight_state:
                #learn_file.append(state)
        missing_state = {
            "Missing_State": learning_list

        }

        new_lear_file = pd.DataFrame(missing_state)
        new_lear_file.to_csv("missing_States_file.csv")
        break

    if answer_state.title() in theRight_state and answer_state.title() in statesList: 
        print("is already choosen")
    elif  answer_state.title() in statesList:
        theRight_state.append(answer_state.title())
        state = us[us.state == f"{answer_state.title()}"]
        xcor = int(state.x)
        ycor = int (state.y)
        abde.goto(xcor,ycor)
        abde.write(f"{answer_state.title()}")        
        #print(f"is Da X: {xcor} Y: {ycor}")
        SCORE += 1

        if SCORE == 50:
            break


    
        

#How to get coordinate
#--------------------------------------

#def get_cor_mouseclick (x,y):
#    print(x, y)
#turtle.onscreenclick(get_cor_mouseclick)
#turtle.mainloop()

#--------------------------------------



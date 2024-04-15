from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
REPS = 0
COLM = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    labelTimerWork.config(text= "Timer",fg=GREEN)
    canvas.itemconfig(canvasText,text = "00:00")
    LabelHacken.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1
    if REPS  % 8 == 0:
        count_down(LONG_BREAK_MIN)
        labelTimerWork.config(text="Break",fg=RED)
        
    elif REPS  % 2 == 1:
        count_down(WORK_MIN)
        labelTimerWork.config(text="Work",fg=GREEN)
        
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        labelTimerWork.config(text="Break",fg=PINK)
       


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    global REPS
    global COLM
    count_min = math.floor(count/60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec =f"0{count_sec}"
        

    canvas.itemconfig(canvasText,text = f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        hacken = ""
        worksession = math.floor(REPS/2)

        for _ in range (worksession):
            hacken+= "✔"
        LabelHacken.config(text=hacken)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224, bg= YELLOW, highlightthickness=0)
tomatePic = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image =tomatePic)
canvasText = canvas.create_text(100,134,text= "00:00", fill="white", font= (FONT_NAME,28,"bold"))
canvas.grid(row=1,column=1)



labelTimerWork = Label(text="Timer",font=(FONT_NAME,32,"bold"),fg=GREEN,bg=YELLOW)
labelTimerWork.grid(row=0,column=1)

StartButton = Button(text="Start",width=4,command=start_timer)
StartButton.grid(row=2,column=0)

ResetButton = Button(text="Reset",width=4, command= reset_timer)
ResetButton.grid(row=2,column=2)

LabelHacken = Label(font= (FONT_NAME,15,"bold"), fg= GREEN, bg= YELLOW)
LabelHacken.grid(row=4,column=1)
























window.mainloop()
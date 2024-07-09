from tkinter import *
from data import question_data 

for question in question_data:
    qz = question["question"]
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.canvas = Canvas(width= 300, height=250)
        Scoretext = Label(text= "Hello World", font=("Arial", 10 ), background=THEME_COLOR,foreground="white")
        canvas_text2 = self.canvas.create_text(150,125,text= qz,  fill="black",font=("Arial", 20, "italic"))
        self.canvas.grid(row=1,columnspan=2, pady=20)
        Scoretext.grid(row=0,column=1)

        xPic = PhotoImage(file="congenial-computing-machine/quizzler_Api/images/false.png")
        yPic = PhotoImage(file="congenial-computing-machine/quizzler_Api/images/true.png")
        self.x = Button(image=yPic)
        self.y = Button(image=xPic)
        self.x.grid(row=2,column=0, padx=20, pady=20)
        self.y.grid(row=2,column=1, padx=20, pady=20)
        self.window.mainloop()

uh = QuizInterface()
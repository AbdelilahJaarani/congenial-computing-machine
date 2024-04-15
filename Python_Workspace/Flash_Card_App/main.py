from tkinter import*
import random
import pandas

BACKGROUND = "#B1DDC6"

data = pandas.read_csv("data\Arabic_German.csv")
 # "orient" Showing like how the dict should be sort 
current_card = {}
to_learn ={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/Arabic_German.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")






def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(title,text ="Arabic",fill = "black")
    canvas.itemconfig(txt, text = current_card["Arabic"], fill = "black")
    canvas.itemconfig(background, image=card_front_img)
    window.after(3000, func= flip_card)
   
    
def is_known():
    
    to_learn.remove(current_card) 
    print(len(to_learn))
    dt = pandas.DataFrame(to_learn)
    dt.to_csv("data/words_to_learn.csv", index = False)
    next_card()


def flip_card():
    canvas.itemconfig(title,text ="German", fill= "white")
    canvas.itemconfig(txt, text = current_card["German"], fill = "white")
    canvas.itemconfig(background, image=card_back_img)



window = Tk()
window.title ("Flashy")
window.config(padx=50,pady=50, bg= BACKGROUND)
window.after(3000, func= flip_card)




#def randomWord():
    
    #data= []
    #with open ("data\Arabic_German.csv", "r",encoding="utf8") as arabicfile:
        #word = csv.DictReader(arabicfile)
        #for row in word:
            #data.append(row['Arabic'])
            #data.append(row['German'])
    #canvas.itemconfig(txt,text=random.choice(data))


# 
canvas = Canvas(width=800, height= 526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400,263,image= card_front_img)
title = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))

canvas.grid(row=0,column=0, columnspan=2)
canvas.config(bg=BACKGROUND,highlightthickness=0)
txt = canvas.create_text(400,263,text= "", font=("Ariel",60,"bold"))
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)


check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image,highlightthickness=0,command=is_known)
check_button.grid(row=1,column=1)


next_card()  

window.mainloop()
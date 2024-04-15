import tkinter

window = tkinter.Tk()


window.title("GUI MY FIRST ONE ")
window.minsize(width=500,height=300)
TEXT = "I am a Label"

def buttonClicked():
    my_label["text"] = input.get()
    


#Label

my_label =tkinter.Label(text= TEXT, font = ("Arial", 24 ))
my_label.grid(row=0,column=0)


#Button
button = tkinter.Button(text= "click me", command= buttonClicked)
button.grid(row=1,column=1)

#Button
button2 = tkinter.Button(text= "Click2", command= buttonClicked)
button2.grid(row=0,column=2)

#Entry
input= tkinter.Entry(width= 30)
input.grid(row=3,column=3)

window.mainloop()
import tkinter

window = tkinter.Tk()


window.title("GUI MY FIRST ONE ")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)
TEXT = "I am a Label"

def buttonClicked():
    my_label["text"] = input.get()
    


#Label

my_label =tkinter.Label(text= TEXT, font = ("Arial", 24 ))
my_label.pack()


#Button
button = tkinter.Button(text= "click me", command= buttonClicked)
button.pack()

#Entry
input= tkinter.Entry(width= 30)
input.pack()

#Text
text = tkinter.Text(height=5, width=30)

#Puts cursor in textbox.
text.focus()

#Adds some text to begin with
text.pack()

#SpinBox

def spinboxUsed():

    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0,to=10,width=5,command=spinboxUsed)
spinbox.pack()


#That is the function which it is used after clicking on the scale 
def scaleUsed(value):
    print (value)

scale = tkinter.Scale(from_=0, to= 100, command= scaleUsed)
scale.pack()

#Checkbuttonm 

def checkbuttenUsed():
    print(checkState.get())
    

checkState = tkinter.IntVar()
chekbutton = tkinter.Checkbutton(text="Is On?",variable=checkState,command= checkbuttenUsed)
checkState.get()
chekbutton.pack()

def RadioButtonUsed():
    print(radioButtonChecked.get())
    

radioButtonChecked = tkinter.IntVar()
radioButton = tkinter.Radiobutton(text= "Option1", value= 1, variable = radioButtonChecked,command =RadioButtonUsed)
radioButton2 = tkinter.Radiobutton(text= "Option2", value= 2, variable = radioButtonChecked, command=RadioButtonUsed)

radioButton.pack()
radioButton2.pack()

def listbox_used(event):
   # print(listbox.get(listbox.curselection()))
   print("Hello")
   


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListbioxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
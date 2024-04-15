import tkinter

window = tkinter.Tk()


window.title("Km to miles calculator")
window.minsize(width=200,height=60)
window.config(padx=50,pady=50)

def buttonCalculatClicked():
    kmSolution = int(input.get())/0.62
    labelKmNumber["text"] = round(kmSolution,2)


input_text = tkinter.StringVar()
input = tkinter.Entry(width=10, textvariable= input_text, justify="center")
input.grid(row=0,column=1)
input_text.set("0")

labelMiles = tkinter.Label(text="Miles")
labelMiles.grid(row=0,column=2)

labelKm = tkinter.Label(text= "Km")
labelKm.grid(row=1,column=2)

labelIsEqual = tkinter.Label(text="is equal to")
labelIsEqual.grid(row=1,column=0)

labelKmNumber = tkinter.Label(text="0")
labelKmNumber.grid(row=1,column=1)


buttonCalculate = tkinter.Button(text= "Calculate", command= buttonCalculatClicked)
buttonCalculate.grid(row=2,column=1)








window.mainloop()
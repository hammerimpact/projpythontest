from tkinter import *

root = Tk()

myEntry = Entry(root, width=50, fg="white", bg="blue")
myEntry.pack()
myEntry.insert(0, "enter text")

def myClick():
    textValue = myEntry.get()
    if not textValue:
        textValue = "None"
    myLabel = Label(root, text=textValue, fg="red", bg="black")
    myLabel.pack()

myButton = Button(root, text = "Click Me", padx=60, pady=60, command=myClick, fg="white", bg="#000000")
myButton.pack()

myButton2 = Button(root, text="haha", state=DISABLED, padx= 200, pady=50)
myButton2.pack()

root.mainloop()
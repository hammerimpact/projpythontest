from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("test checkbox")
root.geometry("300x300")

# intvar
var = IntVar()

def onclickcheck():
    print(var.get())

c1 = Checkbutton(root, text="int var!", variable=var, command=onclickcheck)
c1.select()
c1.pack()

# string var
strVar = StringVar()

def onclickcheck2():
    print(strVar.get())

c2 = Checkbutton(root, text="str var!", variable=strVar, command=onclickcheck2, onvalue="onon", offvalue="offoff")
c2.deselect()
c2.pack()

root.mainloop()
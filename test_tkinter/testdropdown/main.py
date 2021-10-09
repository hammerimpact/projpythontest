from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("test dropdown")
root.geometry("300x300")



lst = ["Monday", "Tuesday", "Wednesday"]

clicked = StringVar()
clicked.set(lst[0])

def onclickmenu(p1):
    print(clicked.get())
drop = OptionMenu(root, clicked, *lst, command=onclickmenu)
drop.pack()


root.mainloop()
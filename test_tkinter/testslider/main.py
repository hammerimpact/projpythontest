from tkinter import *

root = Tk()
root.title("test slider")
root.geometry("300x300")

lblInfo = Label(root, text="None")
lblInfo.pack()

def Refresh(num):
    lblInfo['text'] = f"h:{horizontal.get()} v:{vertical.get()}"
    root.geometry(f"{horizontal.get()}x{vertical.get()}")

horizontal = Scale(root, from_=300, to=500, orient=HORIZONTAL, command=Refresh)
horizontal.pack()

vertical = Scale(root, from_=300, to=500, orient=VERTICAL, command=Refresh)
vertical.pack()

Refresh(0)

root.mainloop()
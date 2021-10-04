from tkinter import *

root = Tk()
root.title("radiobutton test")
root.geometry("300x150")

r = StringVar()
r.set("NONE")

myLabel = Label(root, text=r.get())
myLabel.pack(anchor=W)

def OnClick():
    myLabel['text'] = r.get()

Radiobutton(root, text="North", variable=r, value="__North", command=OnClick).pack(anchor=N)
Radiobutton(root, text="East", variable=r, value="__East", command=OnClick).pack(anchor=E)
Radiobutton(root, text="West", variable=r, value="__West", command=OnClick).pack(anchor=W)
Radiobutton(root, text="South", variable=r, value="__South", command=OnClick).pack(anchor=S)

root.mainloop()
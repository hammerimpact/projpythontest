from tkinter import *

root = Tk()
root.title("TestFrame01")

frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

btn = Button(frame, text="Don't Click here")
btn.grid(row=0, column=0)

btn2 = Button(frame, text="Click!")
btn2.grid(row=1, column=0)

root.mainloop()
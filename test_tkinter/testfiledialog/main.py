from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("test file dialog")

def open() :
    fileName = filedialog.askopenfilename(initialdir="./images", title="test", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("all", "*.*")))
    global imgFile
    imgFile = ImageTk.PhotoImage(image=Image.open(fileName))
    lblImg = Label(root, image=imgFile)
    lblImg.pack()
    
btn = Button(root, text="open", command=open)
btn.pack()
root.mainloop()
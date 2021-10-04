from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("test new indows")
root.geometry("400x400")

Label(root, text="Root").pack()

def OnClickOpen():
    global imgTop
    
    top = Toplevel()
    top.title("TopLevel")
    lblTitle = Label(top, text="Top")
    lblTitle.pack()

    btn = Button(top, text="Close", command=top.destroy)
    btn.pack()

    imgTop = ImageTk.PhotoImage(image=Image.open("./test_tkinter/testnewwindows/images/test02.jpg"))
    lblImage = Label(top, image=imgTop)
    lblImage.pack()
    

Button(root, text="open", command=OnClickOpen).pack()


root.mainloop()
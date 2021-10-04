from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Test MessageBox")
root.geometry("400x400")

def OnClickShowInfo(): messagebox.showinfo("showinfo!", "showinfo")
def OnClickShowWarning(): messagebox.showwarning("showwarning!", "showwarning")
def OnClickShowError(): messagebox.showerror("showerror!", "showerror")
def OnClickAskOKCancel(): messagebox.askokcancel("askokcancel!", "askokcancel")
def OnClickAskQuestion(): messagebox.askquestion("askquestion!", "askquestion")
def OnClickAskYesNo(): 
    result = messagebox.askyesno("askyesno!", "askyesno")
    if result :
        messagebox.showinfo("info", "click yes")
    else :
        messagebox.showinfo("info", "click no")

Button(root, text="showinfo", command=OnClickShowInfo).pack()
Button(root, text="showwarning", command=OnClickShowWarning).pack()
Button(root, text="showerror", command=OnClickShowError).pack()
Button(root, text="askokcancel", command=OnClickAskOKCancel).pack()
Button(root, text="askquestion", command=OnClickAskQuestion).pack()
Button(root, text="askyesno", command=OnClickAskYesNo).pack()


root.mainloop()
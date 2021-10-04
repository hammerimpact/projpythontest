from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.delete(0)

lstButtons = []

def OnClickNumber(num):
    inputTxt = e.get()
    e.delete(0, END)
    e.insert(0, inputTxt + str(num))

def OnClickPlus():
    return

def OnClickMinus():
    return

def OnClickEqual():
    return

def OnClickClear():
    e.delete(0, END)

def AddButton(i, _text, func):
    btn = Button(root, text=_text, padx=40, pady=20, command=func)
    btn.grid(row= 1 + int(i / 3), column=i % 3)
    lstButtons.append(btn)

def AddNumberButton(i, _text, nIndex):
    AddButton(i, _text, lambda: OnClickNumber(nIndex))

for i in range(0, 9):
    AddNumberButton(i, str(i + 1), i + 1)

AddNumberButton(9, str(0), 0)
AddButton(10, "+", OnClickPlus)
AddButton(11, "-", OnClickMinus)
AddButton(12, "=", OnClickEqual)
AddButton(13, "Clr", OnClickClear)

root.mainloop()
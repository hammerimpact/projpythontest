import os

from tkinter import *
from PIL import ImageTk, Image

class AppSetting:
    def __init__(self) -> None:
        self.width = 800
        self.height = 1024
        self.imageWidth = int(self.width * 0.8)
        self.imageHeight = int(self.height * 0.8)
        self.nIndex = 0
        self.nCount = 0
        self.lstFilePaths = []
        self.strCurPath = ''

    def AddIndex(self, v) :
        self.nIndex += v
        if (self.nIndex < 0):
            self.nIndex = self.nCount - 1
        if (self.nIndex >= self.nCount):
            self.nIndex = 0

    def RefreshData_CurPath(self) : 
        self.strCurPath = self.lstFilePaths[self.nIndex]

# global variable
pAppSetting = AppSetting()


def Init():
    for r,d,f in os.walk("./test_tkinter/imageviewer/images"):
        for filename in f:
            if '.jpg' in filename or '.png' in filename :
                pAppSetting.lstFilePaths.append(os.path.join(r, filename))

    pAppSetting.nIndex = 0
    pAppSetting.nCount = len(pAppSetting.lstFilePaths)
    if pAppSetting.nCount > 0:
        pAppSetting.strCurPath = pAppSetting.lstFilePaths[pAppSetting.nIndex]
    else:
        pAppSetting.strCurPath = ''

def OnClickPrev():
    # refresh data
    pAppSetting.AddIndex(-1)
    pAppSetting.RefreshData_CurPath()
    # refresh ui
    RefreshUI_Image()
    RefreshUI_Status()

def OnClickNext():
    # refresh data
    pAppSetting.AddIndex(1)
    pAppSetting.RefreshData_CurPath()
    # refresh ui
    RefreshUI_Image()
    RefreshUI_Status()


    
def RefreshUI_Image():
    global imageCache
    _image = Image.open(pAppSetting.strCurPath)

    tpSize = (_image.width, _image.height)

    resizeRate = float(1)
    if tpSize[0] >= pAppSetting.imageWidth:
        resizeRate = float(pAppSetting.imageWidth / tpSize[0])
    tpSize = (int(tpSize[0] * resizeRate), int(tpSize[1] * resizeRate))

    resizeRate = float(1)
    if tpSize[1] >= pAppSetting.imageHeight:
        resizeRate = float(pAppSetting.imageHeight / tpSize[1])
    tpSize = (int(tpSize[0] * resizeRate), int(tpSize[1] * resizeRate))
    
    _image = _image.resize(tpSize, Image.ANTIALIAS)

    imageCache = ImageTk.PhotoImage(image=_image)
    labelImage = Label(image=imageCache)
    labelImage.grid(row=0, column=1)

def RefreshUI_Status():
    global label_status
    label_status['text'] = f"Image {pAppSetting.nIndex + 1} / {pAppSetting.nCount}"

def InitUI_Buttons(_root):
    btnPrev = Button(_root, text="<<", command=OnClickPrev)
    btnPrev.grid(row=1, column=0)
    btnNext = Button(_root, text=">>", command=OnClickNext)
    btnNext.grid(row=1, column=2)
    btnClose = Button(_root, text="Exit App", command=_root.quit)
    btnClose.grid(row=1, column=1)

def InitUI_Status(_root):
    global label_status
    label_status = Label(_root, text="none", bd=1, relief=SUNKEN)
    label_status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def main():
    Init()
    
    root = Tk()
    root.title("image viewer test")
    root.iconbitmap("./test_tkinter/imageviewer/examp_ico.ico")
    root.geometry(f"{pAppSetting.width}x{pAppSetting.height}")

    InitUI_Buttons(root)
    InitUI_Status(root)

    RefreshUI_Image()
    RefreshUI_Status()

    root.mainloop()


# main
main()
from tkinter import *
from subprocess import call   
import cv2
from QR_reader import closeCAM

XY = "720x720"
XL = 730
YW = 720   


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
        
        editMenu = Menu(menu)
        editMenu.add_command(label="QR Reader",command=self.openQR)
        editMenu.add_command(label="QR.png",command=self.QRpng)
        menu.add_cascade(label="QR Options", menu=editMenu)

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        ##how we make buttons and give them functions
        #QRButton = Button(self, text="QR Reqder", command=self.openQR)
        PrintHI = Button(self, text= "Print Hi",command=self.PrintHI)
        Kamera = Button(self, text= "Close Cam", command=self.ReleaseCam)      
        #How we place buttons       
        #QRButton.place(x=350,y=720/2)
        PrintHI.place(x=XL/2,y=YW/2)
        Kamera.place(x=XL/3,y=YW/2)       
    def ReleaseCam(self):
        closeCAM()    
        
    def openQR(self):
        call(["python","QR reader.py"])
    
    def QRpng(self):
        call(["python","1.png"])
    
    def exitProgram(self):
        exit()
    
    def PrintHI(self):
        print("Hi")
        
       
root = Tk()
root.wm_title("Interface")
app = Window(root)
root.geometry(XY)
root.mainloop()
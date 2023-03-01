#code from https://pythonbasics.org/tkinter-button/
from tkinter import *
from subprocess import call   
from PIL import ImageTk, Image

XY = "720x720"
XL = 720
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
                
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        #how we make buttons and give them functions
        #PrintHI = Button(self, text= "Print Hi",command=self.PrintHI,width= 20)            
        #Kamera = Button(self, text= "Close Cam", command=self.ReleaseCam)      
        #How we place buttons       
        
        #Title.place(x=(XL),y=YW/5)
        #Kamera.place(x=XL/3,y=YW/2)
        Label(self,text="Interface for Program",font=('Helvetica bold', 25),fg="green").pack(pady=20)
        QRButton = Button(self, text="QR Reader", command=self.openQR,fg= "white",bg="black", width= 20)
        PrintHI = Button(self, text="Print Hi", command=self.PrintHI,fg= "white",bg="black", width= 20)
        
        QRButton.place(x=XL/2-90,y=((YW/2)-30))
        PrintHI.place(x=XL/2-90,y=YW/2)       
    
    def openQR(self):
        call(["python","QR_reader.py"])
    
    def exitProgram(self):
        exit()
    
    def PrintHI(self):
        print("Hi")  
       
root = Tk()
root.wm_title("Main Interface")
app = Window(root)
root.geometry(XY)
root.mainloop()
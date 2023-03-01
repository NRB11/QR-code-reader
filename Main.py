#code from https://pythonbasics.org/tkinter-button/
from tkinter import *
from subprocess import call   
from PIL import ImageTk, Image

XY = "720x720"
XL = 720
YW = 720   

root = Tk()
root.wm_title("Main Interface")
root.geometry(XY)

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
        
        QRMenu = Menu(menu)      
        menu.add_cascade(label="QR",menu=QRMenu)
        
        QRCodeMenu = Menu(menu)
        QRCodeMenu.add_command(label="Front Page QR Code",command=self.QRCodeFront)
        QRCodeMenu.add_command(label="QR yt",command=self.QRCodeExtra1)
        QRMenu.add_cascade(label="QR Codes", menu=QRCodeMenu)
        """
        QR = Menu(menu, tearoff = 0)
        QR.add_command(label="QR codes")
        menu.add_cascade(label = "File", menu = QR)
        QR.add_cascade(label = "QR Front img", menu = QR)
       
        QRMenu = Menu(menu,tearoff=0)
        QRMenu.add_command(label="QR Front img", command=self.QRCode)
        menu.add_cascade(label = "QR", menu = QR)
        menu.add_cascade(label = "QRCode", menu = QRMenu)
        """
             
        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        """
        frame = Frame(root, width=400, height=300)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        
        img = ImageTk.PhotoImage(Image.open("Front_Pic.png")) 
        """
        #how we make buttons and give them functions
        #PrintHI = Button(self, text= "Print Hi",command=self.PrintHI,width= 20)            
        #Kamera = Button(self, text= "Close Cam", command=self.ReleaseCam)      
        #How we place buttons       
        
        #Title.place(x=(XL),y=YW/5)
        #Kamera.place(x=XL/3,y=YW/2)
        Label(self,text="Interface for Program",font=('Helvetica bold', 25),fg="green").pack(pady=20)
        QRButton = Button(self, text="QR Reader", command=self.openQR,fg= "white",bg="black", width= 20)
        PrintHI = Button(self, text="Print Hi", command=self.PrintHI,fg= "white",bg="black", width= 20)
        #label = Label(frame, image = img)
        #label.pack()
      
        
        QRButton.place(x=XL/2-90,y=((YW)-100))
        PrintHI.place(x=XL/2-90,y=((YW)-150))       
        #label.place(x=XL/2,y=YW/2-100)
        
          
    def openQR(self):
        call(["python","QR_reader.py"])
    
    def QRCodeFront(self):
        call(["python","FrontImage.py"])
    def QRCodeExtra1(self):
        call(["python","Images\QR_yt_song.png"])
    
    def exitProgram(self):
        exit()
    
    def PrintHI(self):
        print("Hi")  
      
app = Window(root)
root.mainloop()
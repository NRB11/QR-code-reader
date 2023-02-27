import cv2
from pyzbar.pyzbar import decode
import time
from subprocess import call


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
used_code = []

def open_box1_py():
    call(["python", "Box1.py"])

camera = True
while camera == True:
    success, frame = cap.read()
    
    for code in decode(frame):
        QRCode = code.data.decode('utf-8')
        match QRCode:
            case "1":
                open_box1_py()
                time.sleep(5)
            case "2":
                print("box 2")
                time.sleep(5)
            case "3":
                print("box 3")
                time.sleep(5)
            case "4":
                print("box 4")
                time.sleep(5) 
    
    cv2.imshow('Testing_QR_scanner', frame)
    cv2.waitKey(1)
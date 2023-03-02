import cv2
from pyzbar.pyzbar import decode
import time
from subprocess import call

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
used_code = []
Hight = 640
Width = 480
cx = int(Hight/2)
cy = int(Width/2)

center_coords = (cx,cy)

thickness = 10
color = (0, 0, 0)
start_point = cx - 80, cy - 80
end_point = cx + 80, cy + 80 

def closeCAM():
        cv2.destroyAllWindows()

camera = True
while camera == True:
    success, frame = cap.read()
    cv2.rectangle(frame, start_point, end_point, color, thickness)
   
    
    for code in decode(frame):
        QRCode = code.data.decode('utf-8')  
        match QRCode:
            case "1":
                def open_box1_py():
                    call(["python", "QR\Box1.py"])
                    
                open_box1_py()
                time.sleep(5)
            
            case "2":
                print("box 2")
                time.sleep(5)
            
            case "3":
                print("box 3")
                time.sleep(5)
            
            case "4":
                print("Stoped")
                camera = False
                time.sleep(5)
        """    
        pixel_center_bgr = frame[cx, cy]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
        cv2.putText(frame, str(QRCode), (10,50), 0, 1, (b, g, r), 2)
        cv2.circle(frame, (cy, cx), 5, (25, 25, 25), 3)
        """                
    
    cv2.imshow('Testing_QR_scanner', frame)
    cv2.waitKey(1)
closeCAM()
    
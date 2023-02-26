import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('QR_yt_song.png')
print(decode(img))
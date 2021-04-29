import cv2
from pyzbar.pyzbar import decode
import numpy as np

cap=cv2.VideoCapture(0); #create a videocapture object with webcam
cap.set(3,700); #set width of capture
cap.set(4,900); #set height of capture

cv2.namedWindow('Decode',cv2.WINDOW_NORMAL); #create a named window

while True:
    ret,frame=cap.read(); #read frame
    if ret ==True:
        for code in decode(frame):
            print(code);
            code_data=code.data.decode('utf8'); #get the qr or barcode data and decode in utf8
            poly_points=np.array([code.polygon],np.int32); #create an array of polygon points
            rect_pts=code.rect; #get the rect value of qrcode

            cv2.polylines(frame,[poly_points],True,(255,255,3),4);#create a poyline on image
            cv2.putText(frame,code_data,(rect_pts[0],rect_pts[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2); #put text on image

    cv2.imshow('Decode',frame); #show image

    if cv2.waitKey(20)&0xFF==ord('q'):
        break;

cv2.destroyWindow('Decode'); #destroy window

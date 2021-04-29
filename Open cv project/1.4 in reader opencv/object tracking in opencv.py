'''We can use the colorspace change to track object
1) Read the frame
2)Convert the color space to hsv
3)Threshold for the color
4)Extract the image
'''
import cv2
import numpy as np

cap=cv2.VideoCapture(0); #create a video capture object

while (cap.isOpened()):
    ret,frame=cap.read(); #read capture

    if ret==True:
        hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV); #convert color from bgr -> hsv

        lower_red=np.array([-10,50,50]); #cretae an array object
        upper_red=np.array([10,255,255]); #create an array object

        #==> Threshold for red
        mask=cv2.inRange(hsv_frame,lower_red,upper_red); #Threshold color in range

        res=cv2.bitwise_and(frame,frame,mask=mask); #conbine frame and mask

        cv2.imshow('Frame',frame); #image show
        cv2.imshow('Mask',mask); #Image show
        cv2.imshow('res',res); #image show in window res

        if cv2.waitKey(5)&0xFF==ord('q'):
            break;

cv2.destroyWindow(); #destroy all windows

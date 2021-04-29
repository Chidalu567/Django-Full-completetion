import cv2
import numpy as np
#Dilation increases the size of the binary image if any of the pixel under kernel is 1

img=cv2.imread('Letter.png',cv2.IMREAD_COLOR); #image read in color

kernel=np.ones((5,5),np.float32); #create a 5x5 kernel

res=cv2.dilate(img,kernel,iterations=1); #erode image for noise

cv2.namedWindow('Dilation',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Dilation',res); #image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Dilation'); #destroy window

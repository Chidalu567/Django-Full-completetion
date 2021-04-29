import cv2
import numpy as np
#Erosion reduces the size of the binary image and removes all pixel close to the boundary if the value under the kernel is not 1

img=cv2.imread('Letter.png',cv2.IMREAD_COLOR); #image read in color

kernel=np.ones((5,5),np.float32); #create a 5x5 kernel

res=cv2.erode(img,kernel,iterations=1); #erode image for noise

cv2.namedWindow('Erosion',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Erosion',res); #image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Erosion'); #destroy window

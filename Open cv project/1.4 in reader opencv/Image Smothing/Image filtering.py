import cv2
import numpy as np
'''We use c2.filter2D() to filter image'''

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #image read in color

kernel=np.ones((5,5),np.float32)/25; #create a one array
filtered_image=cv2.filter2D(img,-1,kernel); #filter2D image with kernel and a depth of -1

cv2.namedWindow('Original',cv2.WINDOW_NORMAL); #create a named window
cv2.namedWindow('Result',cv2.WINDOW_NORMAL); #create a named window

cv2.imshow('Original',img); #Image show in window Original
cv2.imshow('Result',filtered_image);#image show in Window result
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Original'); #destroy window
    cv2.destroyWindow('Result'); #destrpy window

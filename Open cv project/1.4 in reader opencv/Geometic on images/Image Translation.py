import cv2
import numpy as np

'''We use the wrapAffine() to translate images with a give matrix and size of image'''
img=cv2.imread('Eva.jpg',cv2.IMREAD_COLOR); #image read in color
width,height=img.shape[:2]; #thois gives the shape of image

M=np.float32([[1,0,100],[0,1,100]]); #create a float32 array

res=cv2.warpAffine(img,M,(width,height)); #wrapAffine

cv2.namedWindow('Translate',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Translate',res); #image show
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Translate'); #destroy window

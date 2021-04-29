import cv2
import numpy as np

img=cv2.imread('thunder.png',cv2.IMREAD_COLOR); #image read incolor

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr to gray

ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY); #threshold image for value using binary threshold

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image

#===>Rotated rectangle around image
rect=cv2.minAreaRect(cnt[0]); #minimum area of rectangle of contour
box=cv2.boxPoints(rect); #boxpoints of rectangle
box=np.int0(box); #make an array of box

img_c=cv2.drawContours(img,[box],0,(255,255,3),3); #drawcontours around image

cv2.namedWindow('Rotated',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Rotated',img_c); #image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Rotated'); #destroy window rotated

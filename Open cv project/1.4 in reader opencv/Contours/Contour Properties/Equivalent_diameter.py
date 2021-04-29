import cv2
import numpy as np

img=cv2.imread('Rectangle.png',cv2.IMREAD_COLOR); #image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr 2 gray

ret,thresh=cv2.threshold(img_gray,100,200,cv2.THRESH_BINARY); #threshold image for value

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image

'''Equivalent diameter is the diameter of circle with area same as contour area'''
cnt_area=cv2.contourArea(cnt[0]); #contour area
equ_diameter=np.sqrt((4*cnt_area)/np.pi); #square root of 4*contourarea / pi
print(equ_diameter);

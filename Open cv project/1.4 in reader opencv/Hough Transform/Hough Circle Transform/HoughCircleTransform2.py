import cv2
import numpy as np

img=cv2.imread('eyes.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
img_blur=cv2.medianBlur(img_gray,5); #medianBlur image with 5 kernel

circles=cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,50,param1=20,param2=30,minRadius=90,maxRadius=100); #houighcircles

circles=np.uint16(np.around(circles)); #convert to uint16 bot
print(circles)

for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),3); #draw circle on image
    cv2.circle(img,(i[0],i[1]),7,(0,0,255),4); #draw circle on image

cv2.namedWindow('HoughCircle',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('HoughCircle',img); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('HoughCircle'); #destroy window

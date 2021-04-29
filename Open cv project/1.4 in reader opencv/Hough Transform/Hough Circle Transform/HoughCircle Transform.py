import cv2
import numpy as np

img=cv2.imread('coins.png',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
median_blur_img=cv2.medianBlur(img_gray,5); #medianBlur image

circles=cv2.HoughCircles(median_blur_img,cv2.HOUGH_GRADIENT,1,20,param1=10,param2=50,minRadius=90,maxRadius=120); #houghcircles around image

circles=np.uint16(np.around(circles)); #convert to 16 bit
print(circles[0,:])


for a in circles[0,:]:
    cv2.circle(img,(a[0],a[1]),a[2],(0,255,0),2); #draw circle on image
    cv2.circle(img,(a[0],a[1]),2,(0,0,255),3); #draw circle on image

cv2.imshow('HoughCircle',img); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

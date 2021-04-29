import cv2
import numpy as np

img=cv2.imread('road2.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,50,100,cv2.THRESH_BINARY); #threshold for a value

minlinelength=200;
maxlinegap=20;

res=cv2.HoughLinesP(thresh,1,np.pi/180,minlinelength,maxlinegap); #houghlineprobalility

for i in range(len(res)):
    for x1,y1,x2,y2 in res[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3); #draw line on image

cv2.namedWindow('HoughLine',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('HoughLine',img); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('HoughLine'); #destroy window

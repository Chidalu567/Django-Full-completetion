import cv2
import numpy as np

img=cv2.imread('sudoku.jpg',cv2.IMREAD_COLOR); #image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

gaus_blur=cv2.GaussianBlur(img_gray,(5,5),0); #gaussianblur of image

edge=cv2.Canny(gaus_blur,100,200,apertureSize=5); #canny edge detection of image(gaussianBlur image)

minLineLength=200;
maxLineGap=10;

res=cv2.HoughLinesP(edge,1,np.pi/180,minLineLength,maxLineGap); #houghline probalility

for i in range(len(res)):
    for x1,y1,x2,y2 in res[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),4); #draw line on image



cv2.namedWindow('HoughLine',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('HoughLine',img); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('HoughLine'); #destroy window

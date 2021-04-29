import cv2
'''We use the cv2.contourArea() to find the area of contour'''

img=cv2.imread('Rectangle.png',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #covert color from bgr to gray

ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY); #create a simple threshold

contours,highrachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #FIND contour around image

#===>The cv2.approxPolyDp() needs the elipson which is a percentage of the arclength
perimeter=cv2.arcLength(contours[0],True); #archlength of contours
print(perimeter)

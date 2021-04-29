import cv2

'''We use the cv2.contourArea() to find the area of contour'''

img=cv2.imread('malform.png',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #covert color from bgr to gray

ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY); #create a simple threshold

contours,highrachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #FIND contour around image

epsilon=0.7*cv2.arcLength(contours[0],True);#percentage of arcLength of contours for closed shape
approx_contour=cv2.approxPolyDP(contours[0],epsilon,True); #create an approxPolyDP around shape

res=cv2.drawContours(img,contours,-1,(255,255,3)); #draw contours around image

cv2.namedWindow('Approx Method',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Result',res); #Image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Approx Method'); #destroy window

print('hi');

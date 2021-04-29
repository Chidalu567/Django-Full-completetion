import cv2

img=cv2.imread('thunder.png',cv2.IMREAD_COLOR); #image read incolor

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr to gray

ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY); #threshold image for value using binary threshold

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image

#===>Straight bounding rectangle
x,y,w,h=cv2.boundingRect(cnt[0]); #bounding rectangel of contour

rect=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,3),3); #draw rectangle around image

cv2.namedWindow('Rectangle',cv2.WINDOW_NORMAL);#create a named window
cv2.imshow('Rectangle',rect); #image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Rectangle'); #destroy window

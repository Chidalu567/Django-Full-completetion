import cv2

img=cv2.imread('Rectangle.png',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of imagefrom bgr2gray

ret,thresh=cv2.threshold(img_gray,200,500,cv2.THRESH_BINARY); #create a threshold of image

contours,highrachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image

hull=cv2.convexHull(contours[0],returnPoints=True); #conveshull around conves contour


cv2.namedWindow('Hull',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Hull',img_gray); #Image show

print(cv2.isContourConvex(contours[0])); #returns true if contourisconvex

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Hull'); #destroy window

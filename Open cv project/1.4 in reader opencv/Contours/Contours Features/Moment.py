import cv2

#===>The moments contours feature helps in finding centeroid and area of contour

img=cv2.imread('Rectangle.png',cv2.IMREAD_GRAYSCALE); #image read in gray scale

ret,thresh=cv2.threshold(img,100,255,cv2.THRESH_BINARY); #threshold image for values in bumary threshold

contours,highracy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contour arround threshold image

#===>Moments of contour
M=cv2.moments(contours[0]); #moments of contours
Cx=int(M['m10']/M['m00']); #centroid x
Cy=int(M['m01']/M['m00']); #centroid y

print('Value of Centroid x is {}'.format(Cx));
print('Value of Centroid y is {}'.format(Cy));

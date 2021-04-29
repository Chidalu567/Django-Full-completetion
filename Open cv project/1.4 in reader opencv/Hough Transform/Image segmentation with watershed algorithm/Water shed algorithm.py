import cv2
import numpy as np

img=cv2.imread('coin1.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU); #threshold image for a value

#Remove noise
kernel=np.ones((3,3),np.uint8); #create a kernel
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2); #morphological opening for noise(erosion-> dilation)

sure_bg=cv2.dilate(opening,kernel,iterations=3); #dialte image(increasse the boundaries of image)

dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,5); #distance transform of image
ret,sure_fg=cv2.threshold(dist_transform,0.01*dist_transform.max(),255,cv2.THRESH_BINARY); #threshold image for value

sure_fg=np.uint8(sure_fg); #convert the value to int8

not_sure=cv2.subtract(sure_bg,sure_fg); #subtract bg from fg

#Label the regions
ret,markers=cv2.connectedComponents(sure_fg); #apply markers to fg

markers=markers+1;
print(markers)

markers[not_sure==255]=0; #set the marker/label of unknown to zero

markers=cv2.watershed(img,markers); #apply water shed on image
img[markers==-1]=[255,255,3]; #set the border color


cv2.namedWindow('Watershed',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Watershed',img); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Watershed'); #destroy window

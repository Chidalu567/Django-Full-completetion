import cv2
import numpy as np

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #read image in color
allpx=img[100,100]; #this is the pixel value of bgr image
print(allpx);

#===> To get access individual pixel value
pix1=img.item(100,100,0); #this will give the value of first pixel of image
pix2=img.item(100,100,1); #This will give the value of second pixel of image
pix3=img.item(100,100,2); #this will give the value of third pixel of image
print(pix1,pix2,pix3);
#===.Modifying the value of pixel of image
img.itemset((100,100,0),100); #set the new value of first pixel of image
print(img[100,100]);
cv2.imshow('image',img); #show image
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('image'); #destroy window


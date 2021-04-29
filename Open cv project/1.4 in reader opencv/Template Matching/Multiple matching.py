import cv2
import numpy as np
img=cv2.imread('mario.jpg',cv2.IMREAD_COLOR); #image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

template_gray=cv2.imread('coin.jpg',cv2.IMREAD_GRAYSCALE); #image read in grayscale

w,h=template_gray.shape[:2]; #get shape of template

res=cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED); #match template with image

threshold=0.8;#thresold value

loc=np.where(res>=threshold); #maximum location for the method
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),3); #draw rectangle on image

cv2.namedWindow('Multiple matches',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Multiple matches',img); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Multiple matches'); #destroy window

import cv2
import numpy as np

img=cv2.imread('messi2.jpg',cv2.IMREAD_COLOR); #Image read in colot
print(img)
mask_of_img=np.zeros((img[:2]),np.uint8); #create a mask of image

fgmodel=np.zeros((1,65),np.float64); #create a fgmodel
bgmodel=np.zeros((1,65),np.float64); #create a bgmodel

rect=(70,100,450,600); #rectangle

cv2.grabCut(img,mask_of_img,rect,bgmodel,fgmodel,5,cv2.GC_INIT_WITH_RECT); #grabcut image initilize with rectangle

mask2=np.where((mask_of_img==0|mask_of_img==2),0,1).astype('uint8'); #set 0px and 2px to 0 and rest to 1 (1px and 3px,5px and 7px)

img=img*mask2[:,:,np.newaxis]; #multiply mask2 and image to segement the image

cv2.namedWindow('Extract',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Extract',img); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Extract'); #destroy window

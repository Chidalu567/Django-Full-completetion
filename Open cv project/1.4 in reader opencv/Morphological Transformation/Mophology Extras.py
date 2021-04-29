import cv2
import numpy as np

img=cv2.imread('Letter.png',cv2.IMREAD_COLOR); #image read in color

kernel=np.ones((5,5),np.float32); #create a kernel

#===>Opening
m_open=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel); #create a mophology extras of open(erosion->dilation)
m_close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel); #create a morphology extras of close(dilation->erosion)
m_gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel);#CREATE a morphology gradient(erosion-dilation)
'''The rest is blackhat(original_image-close_morphology),tophat(original_image-open_morphology)'''

cv2.imshow('Open',m_open); #Image show
cv2.imshow('Close',m_close); #image show
cv2.imshow('Gradient',m_gradient); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

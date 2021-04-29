import cv2
from matplotlib import pyplot as plt
import numpy as np
img1=cv2.imread('phone.jpg',cv2.IMREAD_COLOR); #Image read in color
img=cv2.imread('phone.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image
#img_gray_32=np.float32(img_gray); #Image gray of float32

res=cv2.goodFeaturesToTrack(img_gray,40,0.05,10); #goodFeaturesToTrack in image
#res=cv2.dilate(res,None); #dilate the result
res=np.int0(res); #convert result to integers

for i in res:
    x,y=i.ravel();
    cv2.circle(img,(x,y),3,(255,0,0),-1); #draw circle on image

plt.subplot(121),plt.imshow(img1),plt.title('Without Shatomasi Corner Detector'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img),plt.title('Sha-Tomasi Corner detector'),plt.xticks([]),plt.yticks([])
plt.show(); #show the plot

cv2.namedWindow('Shatomasi',cv2.WINDOW_NORMAL); #create a namedWindow
cv2.imshow('Shatomasi',img);#image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Shatomasi'); #destroyWindow

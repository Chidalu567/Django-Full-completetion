import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('chessboard.jpg',cv2.IMREAD_COLOR); #Image read in color
img=cv2.imread('chessboard.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from BGR2GRAY
img_gray_32=np.float32(img_gray);#convert img_gray to float32 bit

res=cv2.cornerHarris(img_gray_32,4,3,0.04); #harris corner algorithm on image to find corner in the image

#Dilate result if you like to increase the corner boundary
res=cv2.dilate(res,None); #dilate binary image

img[res>0.43*res.max()]=[255,0,0]; #set the color of corner to red

plt.subplot(121)#sublot if image
plt.imshow(img)#plot image show
plt.title('HarrisCornerDetection'); #title of plot
plt.xticks([]),plt.yticks([]) #x and y ticks

plt.subplot(122),plt.imshow(img1),plt.title('Image Without Harris Corner'),plt.xticks([]),plt.yticks([])
plt.show();#show plot

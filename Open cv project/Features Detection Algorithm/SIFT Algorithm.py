import cv2
from matplotlib import pyplot as plt

img=cv2.imread('fly.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

#==>Using the sift detector
sift=cv2.SIFT_create(); #create sift object
kp,des=sift.detectAndCompute(img_gray,None); #detect and compute keypoints and descriptors in image
print(kp);

res=cv2.drawKeypoints(img_gray,kp,None); #drawKeypoints on image using the keypoint

#plt.subplot(121),plt.imshow(img),plt.title('Original Image'),plt.xticks([]),plt.yticks([])
#plt.subplot(122),plt.imshow(res),plt.title('SIFT image'),plt.xticks([]),plt.yticks([])
#plt.show(); #show the plotKB

cv2.namedWindow('SIFT',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('SIFT',res); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWidow('SIFT'); #destroy window

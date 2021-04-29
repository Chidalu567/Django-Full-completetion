import cv2
from matplotlib import pyplot as plt

img=cv2.imread('goldbar1.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

fast=cv2.FastFeatureDetector_create(threshold=120,nonmaxSuppression=True); #create a fast feature detector object
kp=fast.detect(img_gray,None); #detects keypoint in image

res=cv2.drawKeypoints(img,kp,None,color=(0,255,0)); #draw keypoints on image with keypoint

cv2.namedWindow('FAST',cv2.WINDOW_NORMAL); #create a  named window
cv2.imshow('FAST',res); #imageshow

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('FAST'); #destroy window

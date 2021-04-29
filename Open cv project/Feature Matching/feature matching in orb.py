import cv2
from matplotlib import pyplot as plt

img1=cv2.imread('human.jpg',cv2.IMREAD_COLOR); #image read in color
img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
img2=cv2.imread('human_rotate.jpg',cv2.IMREAD_COLOR); #image read in color
img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

orb=cv2.ORB_create(); #create an orb object
kp1,des1=orb.detectAndCompute(img1_gray,None); #detect and compute keypoints and descriptors on image
kp2,des2=orb.detectAndCompute(img2_gray,None); #detect keypoints and compute descriptors on image

#===>Create a brute-force matcher
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True); #create a bfmatcher
matches=bf.match(des1,des2); #match the descriptors together
matches=sorted(matches,key=lambda x:x.distance); #sort the matches from smallest to highest

res=cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None); #draw 20 matches on image

cv2.namedWindow('BFMatcher in orb',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('BFMatcher in orb',res); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('BFMatcher in orb'); #destroy window



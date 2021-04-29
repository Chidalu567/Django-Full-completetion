import cv2
import numpy as np

img1=cv2.imread('eye.jpg',cv2.IMREAD_COLOR); #Image read in color
img2=cv2.imread('eye_rotate.jpg',cv2.IMREAD_COLOR); #image read in color
img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

#==>Keypoint and descriptor on image
orb=cv2.ORB_create(); #create an orb object
kp1,des1=orb.detectAndCompute(img1_gray,None); #detect and compute keypoints and descriptors on image
kp2,des2=orb.detectAndCompute(img2_gray,None); #detect and compute keypoints and descriptors on image

#===>Create an object matcher
bfm=cv2.BFMatcher(); #create a bruteforce matcher
matches=bfm.knnMatch(des1,des2,k=2); #brute-force match des1 and des2
good=[]; #Python list declaration
for m,n in matches:
    if m.distance>0.07*n.distance:
        good.append(m); #append value to list


if len(good)>10:
    que_loc=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2); #extract the position of query descriptor
    trn_loc=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2); #extract the index location of train descriptor

    M,mask=cv2.findHomography(que_loc,trn_loc,cv2.RANSAC,3.0); #find homography on location of the points and return a perpective of the points and an inliers and outliers
    m_mask=mask.ravel() #create a mask of inliers

    w,h=img1.shape[:2]; #get shape of image
    pts=np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2); #points on image
    dst=cv2.perspectiveTransform(pts,M); #transform to perspective

    img2=cv2.polylines(img2,[np.int32(dst)],True,255,3,cv2.LINE_AA); #draw ploylines on image



else:
    print('There is not enough matches to work with');


draw_params=dict(matchColor=(0,0,255),singlePointColor=None,matchesMask=m_mask,flags=2); #draw match parameters

img3=cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params); #draw matches on image

cv2.imshow('Homography',img3); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

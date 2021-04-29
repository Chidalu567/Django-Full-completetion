import cv2

img1=cv2.imread('eye.jpg',cv2.IMREAD_COLOR); #Image read in color
img2=cv2.imread('eye_rotate.jpg',cv2.IMREAD_COLOR); #Image read in color
img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

#==>Using the sift algorithm
sift=cv2.SIFT_create(); #create a sift object
kp1,des1=sift.detectAndCompute(img1_gray,None); #detect and compute keypoints and descriptors in image
kp2,des2=sift.detectAndCompute(img2_gray,None); #detect and compute keypoints and descriptors in image

bfm=cv2.BFMatcher(); #create a brute-force matcher
matches=bfm.knnMatch(des1,des2,k=2); #knnMatch descriptors toghether
good=[]; #Python list declration

for m,n in matches:
    if m.distance<0.07*n.distance:
        good.append([m]); #append value to list

res=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None); #drawMatchesKnn on images

cv2.namedWindow('BFM.knn ON SIFT',cv2.WINDOW_NORMAL); #create a named windlow
cv2.imshow('BFM.knn ON SIFT',res); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('BFM.knn ON SIFT'); #destroy window

import cv2

img=cv2.imread('fly.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

surf=cv2.xfeatures2d.SURF_create(); #create a surf object with a hessian threshold


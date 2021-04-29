import cv2

img=cv2.imread('Star.png',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,100,200,cv2.THRESH_BINARY); #threshold image for value (thresh binary)

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image

#===>The position of a point on an image
ret=cv2.pointPolygonTest(cnt[0],(190,20),True); #point polygon test
print(ret);

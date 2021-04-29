import cv2

img=cv2.imread('Star.png',cv2.IMREAD_COLOR); #Image read in color
img2=cv2.imread('thunder.png',cv2.IMREAD_COLOR); #image read in color

img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,100,200,cv2.THRESH_BINARY); #threshold image for value (thresh binary)
ret,thresh2=cv2.threshold(img2_gray,100,200,cv2.THRESH_BINARY); #threshold image fo value


cnt1,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image
cnt2,_=cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image

res=cv2.matchShapes(cnt1[0],cnt2[0],1,0.0); #match shapes
print(res);

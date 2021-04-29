import cv2

img=cv2.imread('thunder.png',cv2.IMREAD_COLOR); #image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convertcolor of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,100,300,cv2.THRESH_BINARY); #threshild image binary threshold

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #findcontours around image

#==>For bounding circle
(x,y),radius=cv2.minEnclosingCircle(cnt[0]); #minimum enclosing circle for contour
x=int(x); #interger
y=int(y);#interger
radius=int(radius); #convert to integer

circle=cv2.circle(img, (x,y),radius,(255,255,3),3); #circle image

cv2.namedWindow('Circle',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Circle',circle); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Circle'); #destroy window

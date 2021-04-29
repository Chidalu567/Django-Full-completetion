import cv2

img=cv2.imread('thunder.png',cv2.IMREAD_COLOR); #image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convertcolor of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,100,300,cv2.THRESH_BINARY); #threshild image binary threshold

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #findcontours around image

#==>For bounding Ellipse
ellipse=cv2.fitEllipse(cnt[0]); #fit ellipse for contour
print(ellipse)
Ellipse=cv2.ellipse(img,ellipse,(255,255,3),3); #draw ellipse on img

cv2.namedWindow('Ellipse',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Ellipse',Ellipse); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Ellipse'); #destroy window

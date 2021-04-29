import cv2

img=cv2.imread('map.png',cv2.IMREAD_COLOR); #image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,100,200,cv2.THRESH_BINARY); #threshold image for value (thresh binary)

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around thresh image

#print(cnt)
bottom_part=tuple(cnt[cnt[1][1].argmin()][0]);
top_part=tuple(cnt[cnt[1][1].argmax()][0]);
left_part=tuple(cnt[cnt[1][1].argmin()][-1]);
right_part=tuple(cnt[cnt[1][0].argmax()][0]);

print(top_part)
print(bottom_part);
print(left_part);
print(right_part);

cv2.circle(img,(679,17),13,(255,255,3),-1); #draw circle on image
cv2.circle(img,(785,474),13,(255,255,3),-1); #draw circle on image
cv2.circle(img,(795,473),13,(255,255,3),-1); #draw circle on image
#cv2.circle(img,(679,17),13,(255,255,3),-1); #draw circle on image

cv2.namedWindow('Extreme Point',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Extreme Point',img); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Extreme Point'); #destroy window

import cv2

'''We use findCountours() to find countours and drawCountours() to draw countous'''

img=cv2.imread('Rectangle.png',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert image to grayscale image

ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY); #simple threshold for a value

contours,highracy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #findContours of thresh image
for data in contours:
    print(data)

img_c=cv2.drawContours(img,contours,-1,(255,255,3),3); #draw contours arround image

cv2.circle(img,(229,57),5,(255,255,3),-1); #circle on image
cv2.circle(img,(229,309),5,(255,255,3),-1);#circle on image
cv2.circle(img,(585,309),5,(255,255,3),-1); #circle on image
cv2.circle(img,(585,57),5,(255,255,3),-1); #circle on image

cv2.imshow('thresh',img_c); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

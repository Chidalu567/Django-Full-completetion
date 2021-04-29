import cv2

'''For Image scaling we use cv2.resize()'''

img=cv2.imread('Eva.jpg',cv2.IMREAD_COLOR); #image read in color

cols,rows=img.shape[:2]; #this is the image shape

res=cv2.resize(img,(cols*5,rows*5),interpolation=cv2.INTER_CUBIC); #resize image
cv2.namedWindow('Resize',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Resize',res); #image show on windows
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Resize'); #destroy window

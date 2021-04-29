import cv2

'''Conveting image color space we use cv2.cvtColor()'''
img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of bgr -> gray
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV); #convert color from bgr -> hsv

cv2.namedWindow('image-gray',cv2.WINDOW_NORMAL);#create a named window
cv2.namedWindow('image_hsv',cv2.WINDOW_NORMAL);#create a named window

cv2.imshow('image_gray',img_gray); #Image show in window
cv2.imshow('image_hsv',img_hsv); #image show in window
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('image_gray'); #destroy window
    cv2.destroyWindow('image_hsv'); #destroy window

import cv2

'''The Sobel filter has two types sobelx and sobely'''

img=cv2.imread('Box.png',cv2.IMREAD_GRAYSCALE); #image read in gray scale

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5); #create a sobel filter (x)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5); #create a sobel filter(y)

cv2.namedWindow('Sobelx',cv2.WINDOW_NORMAL); #createa named window
cv2.namedWindow('Sobely',cv2.WINDOW_NORMAL); #createa named window

cv2.imshow('Sobelx',sobelx); #image show in window
cv2.imshow('Sobely',sobely); #Image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

import cv2

img=cv2.imread('image.jpg',cv2.IMREAD_COLOR); #Image read in color
mask=cv2.imread('mask.tif',cv2.IMREAD_GRAYSCALE); #Image read in grayscale

res=cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA); #do an inpaint on image to remove stroke shown on mask from image

cv2.namedWindow('Inpaint',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Inpaint',res); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Inpaint'); #destroy window

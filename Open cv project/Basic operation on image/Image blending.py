import cv2

img1=cv2.imread('Eva.jpg',cv2.IMREAD_COLOR); #Image read in color
img2=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #Image read in color

blend_image=cv2.addWeighted(img1,0.3,img2,0.5,0); #add Weighted to image

cv2.namedWindow('Blend',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Blend',blend_image); #image show in window
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Blend'); #destroy window

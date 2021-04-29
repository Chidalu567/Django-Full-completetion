import cv2


img=cv2.imread('Eva.jpg',cv2.IMREAD_COLOR); #image read in color
width,height,channels=img.shape; #this gives the shape of image

M=cv2.getRotationMatrix2D((width/2,height/2),270,1); #get rotation matrix 2d

res=cv2.warpAffine(img, M,(width,height)); #create a warpAffine

cv2.namedWindow('Rotate',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Rotate',res); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Rotate'); #destroy window

'''Region of image is the region a particular image cover in a larger image
'''
import cv2

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #read imagein normal color
print(img)
imageshape=img.shape; #this returns the full pixel or shape of image
print(imageshape); #this givs the shape of image

#ROI Trying to copy the head and shift toanother place
head=img[:200,300:500]; #region of image
img[100:300,50:250]=head

cv2.namedWindow('image',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('image',img); #image show
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('image'); #destroy window

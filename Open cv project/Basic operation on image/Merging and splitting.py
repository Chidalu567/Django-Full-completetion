'''We mearge and split the rgb of images by indexing in numpy'''
import cv2

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #image read
#===>Merging of channels in image
img[:,:,1]=150; #change the image green to 300

#spliting of channels in image
b=img[:,:,0]; #get the value of image blue
print(b);

cv2.namedWindow('image',cv2.WINDOW_NORMAL);#create a named window
cv2.imshow('image',img); #image show in window
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('image'); #destroy window image

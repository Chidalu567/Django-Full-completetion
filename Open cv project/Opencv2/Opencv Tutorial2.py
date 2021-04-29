import cv2

# #===>Image reading in cv2
# img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #image read in normal color

# #===>Showing image in cv2
# cv2.namedWindow('image',cv2.WINDOW_NORMAL); #create a normal named window
# cv2.imshow('image',img); #show image in window
# cv2.waitKey(0); #wait for key
# cv2.destroyWindow('image'); #destroy window 'image';

#=====>A full project
img=cv2.imread('chidalu.jpg',cv2.IMREAD_GRAYSCALE); #read image in gray scale

cv2.namedWindow('image',cv2.WINDOW_NORMAL); #create a namedwindow
cv2.imshow('image',img); #show image in window
k=cv2.waitKey(0) & 0xFF; #waitfor a key
if k ==27:
    cv2.destroyWindow('image'); #destroy window image
elif k == ord('s'): #if key == s
    cv2.imwrite('chidalu_gray.png',img); #createnew image
    cv2.destroyWindow('image'); #destrpy window image


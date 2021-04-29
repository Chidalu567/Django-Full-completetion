import cv2

img2=cv2.imread('company.png',cv2.IMREAD_COLOR);#image read
img1=cv2.imread('libary.jpg',cv2.IMREAD_COLOR); #image read

#===> Create a region of image
rows,cols,channels=img1.shape; #get the shape of image
roi=img1[0:rows,0:cols]; #create a region of image

#===>mask image and inverse
img1gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY); #convert color of image
ret,mask=cv2.threshold(img1gray,10,255,cv2.THRESH_BINARY); #create a threshold
mask_inv=cv2.bitwise_not(mask); #create an inverse of mask

#===>Black out roi
img_bg=cv2.bitwise_and(roi,roi,mask=mask_inv); #black out  region of image
img_fg=cv2.bitwise_and(img1,img1,mask=mask); #take only te roi of image of logo

dst=cv2.add(img_bg,img_fg); #add images together
img2[0:rows,0:cols]=dst; #replace the roi in image2 with dst

cv2.namedWindow('Show',cv2.WINDOW_NORMAL); #CREATE A named window
cv2.imshow('Show',img2); #image show
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Show'); #destroy window






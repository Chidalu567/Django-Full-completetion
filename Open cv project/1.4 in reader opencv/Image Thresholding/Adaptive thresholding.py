import cv2

#==> Images
img1=cv2.imread('book1.jpg',cv2.IMREAD_COLOR); #image read in color
img2=cv2.imread('book2.jpg',cv2.IMREAD_COLOR); #image read in normal color
img3=cv2.imread('book3.jpg',cv2.IMREAD_COLOR); #image in normal color

#==.Convert image to gray scale
gray_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY); #convert color from bgr 2 gray

blur_img=cv2.medianBlur(gray_img,5); #median blur image by 5

mean=cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2); #create an adaptive thhershold with mean adaptive method

gaussian=cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2); #create an adaptive threshold wit gaussian adaptive method

cv2.namedWindow('mean',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('mean',mean); #Image show in window

cv2.namedWindow('Gaussian',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Gaussian',gaussian); #Image show in window
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('mean'); #destroy window mean
    cv2.destroyWindow('Gaussian'); #destoy window Gaussian

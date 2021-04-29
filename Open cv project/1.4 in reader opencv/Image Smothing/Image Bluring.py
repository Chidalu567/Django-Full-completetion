import cv2

'''We have 4 types of image bluring (average or blur,Gausianblur,medianBlur,Bilateralblur)'''
img=cv2.imread('Night.jpg',cv2.IMREAD_COLOR); #image read in color

#===>For Average blur
avg_blur=cv2.blur(img,(5,5)); #blur image by 5x5 kernel

#===>For Gaussian blur
g_blur=cv2.GaussianBlur(img,(5,5),0); #create a Gaussian blur of image by 5x5 kernel

#===>For medianBlur
M_blur=cv2.medianBlur(img,5); #create a medianBlur of image by 5x5 kernel

#==>For BilateralBlur
B_blur=cv2.bilateralFilter(img,9, 75,75); #create a bilateralFilter

cv2.namedWindow('Averageorblur',cv2.WINDOW_NORMAL); #create a named window
cv2.namedWindow('GaussianBlur',cv2.WINDOW_NORMAL); #create a named window
cv2.namedWindow('MedianBlur',cv2.WINDOW_NORMAL); #create a named window
cv2.namedWindow('BilateralFilter',cv2.WINDOW_NORMAL); #create a named window

cv2.imshow('Averageorblur',avg_blur); #image show
cv2.imshow('GaussianBlur',g_blur); #image show
cv2.imshow('MedianBlur',M_blur); #image show
cv2.imshow('BilateralFilter',B_blur); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window


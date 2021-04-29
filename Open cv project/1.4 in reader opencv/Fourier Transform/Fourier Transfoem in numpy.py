import cv2
import numpy as np

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ft=np.fft.fft2(img_gray); #get frequency transform of image
ft_shift=np.fft.fftshift(ft); #frequecy transform shift to center
magnitude_spectrum=20*np.log(np.abs(ft_shift)); #magnitude spectrum of frequency transform shift

cv2.namedWindow('FT in Numpy',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('FT in Numpy',magnitude_spectrum);#image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('FT in Numpy'); #destroy window

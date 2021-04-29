import cv2
import numpy as np

img_gray=cv2.imread('chidalu.jpg',cv2.IMREAD_GRAYSCALE); #image read in grayscale


ft=np.fft.fft2(img_gray); #frequency transform of image
ft_shift=np.fft.fftshift(ft); #shift 0 frequency to center

#===>HPF we need the inverse of frequency shift and frequency transform
rows,cols=img_gray.shape; #get shape of image
mrows,mcols=int(rows/2),int(cols/2);
ft_shift[mrows-30:mrows+30,mcols-30:mcols+30]=0
i_ft_shift=np.fft.ifftshift(ft_shift); #inverse of frequency shift
i_ft=np.fft.ifft2(i_ft_shift); #Inverse of frequency
img_back=np.abs(i_ft); #absolute of value

cv2.namedWindow('Filter',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Filter',img_back); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Filter'); #destroy window

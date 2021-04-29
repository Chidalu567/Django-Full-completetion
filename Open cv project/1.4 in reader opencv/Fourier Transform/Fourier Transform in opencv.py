import cv2
import numpy as np

img_gray=cv2.imread('chidalu.jpg',cv2.IMREAD_GRAYSCALE); #image read in grayscale

ft=cv2.dft(np.float32(img_gray),flags=cv2.DFT_COMPLEX_OUTPUT); #find frequency transform of image
ft_shift=np.fft.fftshift(ft); #frequency shift

magnitude=20*np.log(cv2.magnitude(ft_shift[:,:,0],ft_shift[:,:,1]));

#===>low pass filter i fourier transform in opencv



cv2.imshow('Frequency',magnitude); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

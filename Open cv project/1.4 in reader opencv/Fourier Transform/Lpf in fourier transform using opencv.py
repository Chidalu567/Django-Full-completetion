import cv2
import numpy as np

img_gray=cv2.imread('chidalu.jpg',cv2.IMREAD_GRAYSCALE); #image read in grayscale

ft=cv2.dft(np.float32(img_gray),flags=cv2.DFT_COMPLEX_OUTPUT); #frequency transform in image
ft_shift=np.fft.fftshift(ft); #frequency transform shift

row,col=img_gray.shape; #get shape of image
mask=np.zeros((row,col,2),np.uint8); #create a mask of image
mrow,mcol=int(row/2),int(col/2);
mask[mrow-30:mrow+30,mcol-30:mcol+30]=1;

ft_shift=mask*ft_shift; #new frequency shift
i_ft_shift=np.fft.ifftshift(ft_shift); #find inverse of frequency transform shift
i_ft=cv2.idft(i_ft_shift); #find inverse of frequency shift

lpf=cv2.magnitude(i_ft[:,:,0],i_ft[:,:,1]); #lowpassfilter

cv2.imshow('LowPassFilter',lpf); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destoryWindow(); #destroy window

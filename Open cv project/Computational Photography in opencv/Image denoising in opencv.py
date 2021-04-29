import cv2
from matplotlib import pyplot as plt

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #Image read in color

res=cv2.fastNlMeansDenoisingColored(img,None,19,10,5,21); #denoise image

plt.subplot(121),plt.title('Original image'),plt.xticks([]),plt.yticks([]),plt.imshow(img)
plt.subplot(122),plt.title('Denoised image'),plt.xticks([]),plt.yticks([]),plt.imshow(res)

plt.show(); #show the plot

cv2.namedWindow('Denoised',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Denoised',res); #image show

cv2.waitKey(0)
cv2.destroyWindow('Denoised')#destroy window

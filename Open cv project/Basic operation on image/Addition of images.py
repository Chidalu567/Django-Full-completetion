import cv2
import numpy as np

img1=np.uint8([200]); #image 1
img2=np.uint8([100]); #Image 2

value=cv2.add(img1,img2); #add image1 and image2 together
print(value)

'''Here We will Access image properties like row,column and channels of image,datatype of image,size of image'''
import cv2
import numpy as np

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #read image in color mode

imgsize=img.size; #this give the size ofimage
print(imgsize);

imgdatatype=img.dtype; #this gives the data type of image
print(imgdatatype);

#===>Shape of image
imgshape=img.shape; #this gives the shape of image
print(imgshape);

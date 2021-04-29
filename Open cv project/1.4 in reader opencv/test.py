import cv2
import numpy as np

green=np.uint8([0,255,0]);
green_hsv=cv2.cvtColor(green,cv2.COLOR_BGR2GRAY)

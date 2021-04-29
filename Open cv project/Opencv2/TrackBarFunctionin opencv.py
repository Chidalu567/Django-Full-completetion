import cv2
import numpy as np

def do_nothing(): #function definition
    pass;

img=np.zeros([512,512,3],np.uint8); #create a zero numpy
cv2.namedWindow('image',cv2.WINDOW_NORMAL); #create a named window

#==>Create trackbars
cv2.createTrackbar('R','image',0,255,do_nothing); #create a trackbar widget
cv2.createTrackbar('G','image',0,255,do_nothing); #create a trackbar widget
cv2.createTrackbar('B','image',0,255,do_nothing); #create a trackbar

switch='o:OFF \n1:ON'; #create a switch
cv2.createTrackbar(switch,'image',0,1,do_nothing); #create a trackbar

while True:
    cv2.imshow('image',img); #show image in window

    r=cv2.getTrackbarPos('R','image'); #get trackbar position
    g=cv2.getTrackbarPos('G','image'); #get trackbar position
    b=cv2.getTrackbarPos('B', 'image'); #get trackbar position
    s=cv2.getTrackbarPos(switch,'image'); #get trackbar position

    if s==0:
        img[:]=0; #change all value in aray to 0
    else:
        img[:]=b,g,r; #change value in array to new value

    if cv2.waitKey(20)&0xFF==ord('q'):
        break;

cv2.destroyWindow('image'); #destroy window

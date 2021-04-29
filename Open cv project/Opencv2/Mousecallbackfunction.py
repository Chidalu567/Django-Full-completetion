import numpy as np
import cv2

def draw_cicle(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),25,(255,255,0),-1); #create a cicle object

img=np.zeros([512,512,3],np.uint8); #create a black background
cv2.namedWindow('image',cv2.WINDOW_NORMAL); #create a named window
cv2.setMouseCallback('image',draw_cicle); #set mouse callback function
while True:
    cv2.imshow('image',img); #show image in window
    if cv2.waitKey(20)&0xFF==ord('q'):
        break
cv2.destroyWindow('image'); #destroy window image

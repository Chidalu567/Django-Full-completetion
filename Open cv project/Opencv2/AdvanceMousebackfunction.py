import cv2
import numpy as np

drawing=False;
mode=True;
ix,iy=-1,-1;

def draw_function(event,x,y,flags,param): #function definition
    global drawing,mode,ix,iy

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y;
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(225,225,3),-1); #draw a rectangle
            else:
                cv2.circle(img,(x,y),25,(255,255,3),-1); #draw a circle
        else:
            pass;
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False;
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,3),-1); #create a rectangle
        else:
            cv2.circle(img, (x,y), 25,(255,255,3),-1); #create a circle on image

img=np.zeros([512,512,3],np.uint8); #create azeros numpy
cv2.namedWindow('image',cv2.WINDOW_NORMAL); #create a named window
cv2.setMouseCallback('image',draw_function); #set mouse call back on window

while True:
    cv2.imshow('image',img); #image show in window
    if cv2.waitKey(20)&0XFF==ord('m'):
        mode=not mode; #change mode to false and draw circle
    if cv2.waitKey(20)&0xFF==ord('q'):
        break;
cv2.destroyWindow('image'); #destroy window

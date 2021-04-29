import cv2
import numpy as np

cap=cv2.VideoCapture('video2.mp4'); #create a capture object
ret,frame1=cap.read(); #read first frame
prv_gray_frame=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray
hsv=np.zeros_like(frame1); #convert frame 1 to hsv using zeroslike
hsv[...,1]=255; #set saturation to 255

while cap.isOpened():
    ret,frame2=cap.read(); #read frame by frame
    next_gray_frame=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY); #convert color of frame from bgr2gray

    flow=cv2.calcOpticalFlowFarneback(prv_gray_frame,next_gray_frame,None,0.3,3,15,3,5,1.2,0); #find the optical flow of object
    mag,ang=cv2.cartToPolar(flow[...,0],flow[...,1]); #cartTo Plor cordinates to find x and y

    hsv[...,0]=ang*180/np.pi/2;
    hsv[...,2]=cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX); #normalize te magnitide

    rgb=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR); #convert color of imag from hsv2bgr

    cv2.namedWindow('DenseOpticalFlow',cv2.WINDOW_NORMAL); #create a named window
    cv2.imshow('DenseOpticalFlow',rgb); #image show

    if cv2.waitKey(5)&0xFF==ord('q'):
        break;

cv2.destroyWindow('DenseOpticalFlow'); #destroy window

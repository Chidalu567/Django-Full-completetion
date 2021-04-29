import cv2
import numpy as np

'''
1] read frist frame
2] get the region of image
3]change to hsv
4]create a mask to remove light
5]calculate the histogram of image
6]normalize the value
7]calculate the BackProject
8]Do a camShift
9]Get the boxPoint
10]add to polylines
11]show image
'''

cap=cv2.VideoCapture(0); #create a capture object

ret,frame=cap.read(); #read first frame
r,h,c,w=250,160,200,400;
track_window=(r,h,c,w);

roi=frame[r:r+h,c:c+w]; #get the region of image
hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV); #convert color of frame from bgr2hsv
lower_red=np.array([-10,50,50]); #lower red
upper_red=np.array([10,255,255]); #upper red
mask=cv2.inRange(hsv_frame,lower_red,upper_red); #threshold for red
tar_hist=cv2.calcHist([hsv_frame],[0],mask,[180],[0,180]); #calculate the histogram of image
cv2.normalize(tar_hist,tar_hist,0,255,cv2.NORM_MINMAX); #normalize the hostogram
term_crit=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1); #term criteria

while cap.isOpened():
    ret,frame=cap.read(); #read frame by frame

    if ret:
        hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV); #convert color of frame from bgr2hsv
        b_p=cv2.calcBackProject([hsv_frame],[0,1],tar_hist,[0,180],1); #calculate backprojection
        ret,res=cv2.CamShift(b_p,track_window,term_crit); #Continous adaptive mean shift


        pts=cv2.boxPoints(ret); #boxpoints of return value
        pts=np.int0(pts); #convert to integer
        img2=cv2.polylines(frame,[pts],True,255,8); #draw polylines on image

        cv2.namedWindow('CamShift',cv2.WINDOW_NORMAL); #create a named window
        cv2.imshow('CamShift',img2); #image show on window

        if cv2.waitKey(90)&0xFF==ord('q'):
            break;
    else:
        break;

cv2.destroyWindow('CamShift'); #destroy window

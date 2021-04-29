import cv2
import numpy as np

cap=cv2.VideoCapture(0); #create a capture object

#Create a track window
r,h,c,w=250,160,200,400;
track_window=(r,h,c,w);

#create a region of image
ret,frame=cap.read(); #read first frame
roi=frame[r:r+h,c:c+w]; #region of image
hsv_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV); #convert color of frame from bgr2hsv
lower_red=np.array([-10,50,50]); #lower gerrn
upper_red=np.array([10,255,255]); #upper green

mask=cv2.inRange(hsv_roi,lower_red,upper_red); #create a treshold of image
hsv_hist=cv2.calcHist([hsv_roi],[0],mask,[180],[0,180]); #calculate histogram of image
cv2.normalize(hsv_hist,hsv_hist,0,255,cv2.NORM_MINMAX); #normalize the histogram

term_crit=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1); #criteria for meanshoift

while True:
    ret,frame=cap.read(); #read frame

    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV); #convert color of frame from bgr2hsv
        b_p=cv2.calcBackProject([hsv],[0,1],hsv_hist,[0,180],1); #calculate backprojection
        ret,track_window=cv2.meanShift(b_p,track_window,term_crit); #do a meanshift for tracked image

        x,y,w,h=track_window;

        img2=cv2.rectangle(frame,(x,y),(x+w,y+h),255,3); #draw a rectangle on image
        cv2.namedWindow('meanShift',cv2.WINDOW_NORMAL); #create a named window
        cv2.imshow('meanShift',img2); #Image show

    if cv2.waitKey(90)&0xFF==ord('q'):
        break;

cv2.destroyWindow('MeanShift'); #destroy window

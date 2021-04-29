import cv2

cap=cv2.VideoCapture(0); #create a videocapture object 'webcam'
out=cv2.VideoWriter('Video6.avi',cv2.VideoWriter_fourcc('m','p','4','v'),20.0,(700,700)); #create a video writer
print(cap.isOpened())
while (cap.isOpened()):
    ret,frame=cap.read(); #read video capture frame by frame
    print(ret);
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY); #convert color of frame to gray
    if ret==True:
        cv2.namedWindow('Video',cv2.WINDOW_NORMAL); #create a named window
        out.write(gray); #write frame or save frame
        cv2.imshow('Video',gray); #image show in window Video
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break

cap.release(); #release capture
out.release(); #release writer
cv2.destroyWindow('Video'); #destroy window Video





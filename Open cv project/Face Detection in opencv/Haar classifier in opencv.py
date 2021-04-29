import cv2

cap=cv2.VideoCapture(0); #create a video capture

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml'); #create a cascade classifier object
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml'); #create an eye cascade object

while cap.isOpened():
    ret,frame=cap.read(); #read frame by frame

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY); #convert color of frame from bgr2gray
    faces=face_cascade.detectMultiScale(gray_frame,1.3,5); #detectmultiscale of frame

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2); #draw rectangle on image

        roi_eye_gray=gray_frame[y:y+h,x:x+h]; #region of image
        roi_eye_color=frame[y:y+h,x:x+h]; #region of image

        eyes=eye_cascade.detectMultiScale(roi_eye_gray); #detect multiscale in image
        print(eyes)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_eye_color,(ex,ey),(ex+50,ey+50),(255,0,0),2); #draw rectangle on image

    cv2.namedWindow('Detect',cv2.WINDOW_NORMAL); #create a named window
    cv2.imshow('Detect',frame); #Image show

    if cv2.waitKey(20)&0xFF==ord('q'):
        break;

cv2.destroyWindow('Detect'); #destroy window

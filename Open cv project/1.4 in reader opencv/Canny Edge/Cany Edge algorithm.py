import cv2

cap=cv2.VideoCapture(0); #create a videocapture object

def do_nothing(): #function definition
    pass;


cv2.namedWindow('Canny',cv2.WINDOW_NORMAL); #create a namedwindow

cv2.createTrackbar('Upper_Threshold','Canny',0,255,do_nothing); #create a trackbar
cv2.createTrackbar('Lower_Threshold','Canny',0,255,do_nothing); #create a trackbar


while cap.isOpened():
    ret,frame=cap.read(); #read frame

    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY); #convert color of frame from bgr2gray

    blur_img=cv2.GaussianBlur(gray_img,(5,5),0); #creatre a gaussian blur

    lw_t=cv2.getTrackbarPos('Upper_Threshold','Canny'); #get the trackbarposition
    up_t=cv2.getTrackbarPos('Lower_Threshold','Canny'); #get the track bar position

    res=cv2.Canny(blur_img,lw_t,up_t,5); #create a canny edge object

    cv2.imshow('Canny',res); #image show in window
    cv2.imshow('Blur',blur_img); #image show
    cv2.imshow('Gray',gray_img); #Image show

    if cv2.waitKey(20)&0xFF==ord('q'):
        break;

cap.release(); #release capture
cv2.destroyWindow(); #destroy window

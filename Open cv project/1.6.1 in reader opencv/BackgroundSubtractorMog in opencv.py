import cv2
from matplotlib import pyplot as plt

cap=cv2.VideoCapture('video2.mp4'); #create a capture object
bg_sub=cv2.createBackgroundSubtractorMOG2(detectShadows=False); #create a background subtractorMOG2 object

while cap.isOpened():
    ret,frame=cap.read(); #Read frame by frame
    mask_res=bg_sub.apply(frame); #apply backgroundsubtractormog2 to frame

    cv2.namedWindow('Foregroundonly',cv2.WINDOW_NORMAL); #create a named window
    cv2.imshow('Foregroundonly',mask_res); #image show

    # plt.subplot(121),plt.imshow(frame),plt.title('Main Video'),plt.xticks([]),plt.yticks([])
    # plt.subplot(122),plt.imshow(mask_res),plt.title('Only Foreground'),plt.xticks([]),plt.yticks([])

    if cv2.waitKey(90)&0xFF==ord('q'):
        break;

cv2.destroyWindow('Foregroundonly'); #destroy window


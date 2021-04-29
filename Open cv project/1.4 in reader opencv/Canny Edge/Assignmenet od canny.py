import cv2
'''The canny edge algorithm is used to find edges in images and videos
1]Read image as grayscale
2]Smoothing the image with Guassian blur for noise
3]Filter gradient with sobel gradient filter
4] Use hysterisis
'''
def do_nothing(): #function definition
    pass;

cv2.namedWindow('Canny',cv2.WINDOW_NORMAL); #create a namedwindow


img=cv2.imread('Workers.jpg',cv2.IMREAD_GRAYSCALE); #image read

blur_img=cv2.GaussianBlur(img,(5,5),0); #GaussianBlur the image

cv2.createTrackbar('Lower_threshold','Canny',0,255,do_nothing);#create a trackbar
cv2.createTrackbar('Upper_threshold','Canny',0,255,do_nothing); #create a trackbar

while True:
    lo_t=cv2.getTrackbarPos('Lower_threshold','Canny'); #get trackbar position
    up_t=cv2.getTrackbarPos('Upper_threshold','Canny'); #get trackbar position

    edge_img=cv2.Canny(img,lo_t,up_t,5); #create a canny object


    cv2.imshow('Canny',edge_img); #Image show in window

    if cv2.waitKey(10)&0xFF==ord('q'):
       break;
cv2.destroyWindow('Canny'); #destroy window


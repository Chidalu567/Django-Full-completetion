import cv2
'''The canny edge algorithm is used to find edges in images and videos
1]Read image as grayscale
2]Smoothing the image with Guassian blur for noise
3]Filter gradient with sobel gradient filter
4] Use hysterisis
'''

img=cv2.imread('Workers.jpg',cv2.IMREAD_GRAYSCALE); #image read

blur_img=cv2.GaussianBlur(img,(5,5),0); #GaussianBlur the image

edge_img=cv2.Canny(img,90,300,4); #create a canny object

cv2.namedWindow('Canny',cv2.WINDOW_NORMAL); #create a namedwindow

cv2.imshow('Canny',edge_img); #Image show in window

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Canny'); #destroy window


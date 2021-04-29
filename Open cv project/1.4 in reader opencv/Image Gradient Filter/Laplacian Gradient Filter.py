import cv2
'''The Laplacian gradient takes only three params the src,flagor datatype and kernel size.Note: source must be a grayscale image'''

img=cv2.imread('Box.png',cv2.IMREAD_GRAYSCALE); #image read in grayscale

laplacian=cv2.Laplacian(img,cv2.CV_64F,ksize=5); #create a laplacian gradient filter
cv2.namedWindow('Laplacian',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Laplacian',laplacian); #Image show in window Laplacian
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Laplacian'); #destroy window Laplacian

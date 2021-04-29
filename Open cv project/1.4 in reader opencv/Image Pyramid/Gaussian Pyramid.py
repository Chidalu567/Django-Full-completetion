import cv2

'''We shall use the Gausian pyramid, to give different resolution if our image'''

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #IMAGE read in color

lower_resolution=cv2.pyrDown(img); #pyramid down from img
higher_reso=cv2.pyrUp(lower_resolution); #pyramid up from lower resolution


cv2.namedWindow('Pyramid Down',cv2.WINDOW_NORMAL); #create a named window
cv2.namedWindow('Pyramid Up',cv2.WINDOW_NORMAL); #create a named window


cv2.imshow('Pyramid Down',lower_resolution); #Image show
cv2.imshow('Pyramid Up',higher_reso); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Pyramid Down'); #destroy window

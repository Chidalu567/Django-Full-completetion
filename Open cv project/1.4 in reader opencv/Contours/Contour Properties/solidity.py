import cv2
'''We use the cv2.contourArea() to find the area of contour'''

img=cv2.imread('Rectangle.png',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #covert color from bgr to gray

ret,thresh=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY); #create a simple threshold

cnt,highrachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #FIND contour around image

'''Extent is the ratio of contour area to convexhull area'''
cnt_area=cv2.contourArea(cnt[0]); #contour area
hull=cv2.convexHull(cnt[0],returnPoints=True); #creatr a convexhull
hull_area=cv2.contourArea(hull); #contour area of hull
Extent=float(cnt_area)/hull_area;
print(Extent);

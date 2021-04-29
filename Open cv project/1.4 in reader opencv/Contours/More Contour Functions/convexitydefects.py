import cv2

img=cv2.imread('Star.png',cv2.IMREAD_COLOR); #Image read in color

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image from bgr2gray

ret,thresh=cv2.threshold(img_gray,100,200,cv2.THRESH_BINARY); #threshold image for value (thresh binary)

cnt,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE); #find contours around image


hull=cv2.convexHull(cnt[0],returnPoints=False); # create a convex hull

defects=cv2.convexityDefects(cnt[0],hull); #find convexity defect in contour and hull

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0];

    start=tuple(*cnt[0][s]);
    print(start)
    end=tuple(*cnt[0][e]);
    #print(end)
    far=tuple(*cnt[0][f]);
    #print(far)


    cv2.line(img,start,end,[255,255,3],3); #draw line on image
    cv2.circle(img,far,3,(0,0,255),-1);#draw circle on image

cv2.namedWindow('Defect',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Defect',img); #image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Defect'); #destroy window defect

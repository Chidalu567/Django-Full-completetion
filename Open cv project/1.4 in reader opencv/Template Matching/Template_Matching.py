import cv2

img=cv2.imread('messi.png',cv2.IMREAD_COLOR);#image read in color
template=cv2.imread('head.png',cv2.IMREAD_COLOR); #Image read in color

w,h=template.shape[:2]; #shape of template

res=cv2.matchTemplate(img,template,cv2.TM_SQDIFF); #match template with image
print(res)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res); #find minimax location of the image

top_left=min_loc; #use this for method of TM_SQDIFF
bottom_left=(top_left[0]+w,top_left[1]+h); #bottom of rextangle

rect=cv2.rectangle(img,top_left,bottom_left,(255,255,3),3); #draw a rectangle on the image

cv2.namedWindow('Matching',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Matching',rect);#image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Matching'); #destroy window matching

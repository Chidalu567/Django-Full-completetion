import cv2
'''We use the function cv2.copymakeborders() to make borders for images only the constant border type takes a value'''

img=cv2.imread('Eva.jpg',cv2.IMREAD_COLOR); #image read in color

#===>For constant border
cv2.namedWindow('constantBorder',cv2.WINDOW_NORMAL); #create a named window
constant=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=[225,225,3]); #create a contant border arround image

#===>For reflect border
cv2.namedWindow('Reflect',cv2.WINDOW_NORMAL); #create a named window
reflect=cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REFLECT); #create a reflect border

#===>For Wrap border
cv2.namedWindow('Wrap',cv2.WINDOW_NORMAL); #create a named window
wrap=cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_WRAP); #create a wrap border

#===>For Replicate border
cv2.namedWindow('Replicate',cv2.WINDOW_NORMAL); #create a named window
replicate=cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REPLICATE); #create a replicate border


cv2.imshow('constantBorder',constant); #image show in window
cv2.imshow('Reflect',reflect); #image show
cv2.imshow('Wrap',wrap); #image show
cv2.imshow('Replicate',replicate); #image show in window

if cv2.waitKey(20)&0xFF==ord('c'):
    cv2.destroyWindow('constantBorder'); #destroy window
elif cv2.waitKey(0)&0xFF==ord('r'):
    cv2.destroyWindow('Reflect'); #destroy window
elif cv2.waitKey(0)&0xFF==ord('w'):
    cv2.destroyWindow('Wrap'); #destroy window
elif cv2.waitKey(0)&0xFF==ord('R'):
    cv2.destroyWindow('Replicate'); #destroy window

import cv2

img=cv2.imread('chidalu.jpg',cv2.IMREAD_COLOR); #Image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); #convert color of image

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml'); #create a cascade classifier object
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml'); #create a cascade classifier object

faces=face_cascade.detectMultiScale(img_gray,1.1,2); #detect multi scale in image gray
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3); #draw rectangle on image

    roi_gray=img_gray[y:y+h,x:x+w]; #roi of eye gray
    roi_color=img[y:y+h,x:x+w]; #roi of eye color

    eyes=eye_cascade.detectMultiScale(roi_gray);#detect multi scale of region of image gray
    print(eyes)
    for ex,ey,ew,eh in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+50,ey+50),(255,0,0),3); #draw rectangle on image

cv2.namedWindow('Detect',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Detect',img); #Image show

cv2.waitKey(0) #wait For a key
cv2.destroyWindow('Detect'); #destroy window

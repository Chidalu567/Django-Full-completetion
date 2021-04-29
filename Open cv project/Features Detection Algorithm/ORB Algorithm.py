import cv2
from matplotlib import pyplot as plt

img=cv2.imread('house.jpg',cv2.IMREAD_COLOR);#image read in color
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);#convert color of image from bgr2gray

orb=cv2.ORB_create(nfeatures=70); #create an orb object
kp=orb.detect(img_gray,None); #detect keypoints on image
print(kp)
res=cv2.drawKeypoints(img,kp,None,color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS);#drawkeypoints on image with keypoint

# plt.subplot(121),plt.imshow(img),plt.title('Origial Image'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(img_gray),plt.title('ORB Algorithm'),plt.xticks([]),plt.yticks([])
# plt.show(); #show plot
cv2.imshow('ORB',res); #Image show

if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

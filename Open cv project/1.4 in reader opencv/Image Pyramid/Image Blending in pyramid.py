import cv2
import numpy as np,sys

S=cv2.imread('F29.jpg'); #image read in color
E=cv2.imread('Eva.jpg'); #image read in color

#==>Creatre a gaussian pyramid of image
Soap=S.copy(); #copy image
Eva=E.copy(); #copy image

gps=[]; #python list declration
gpe=[]; #Python list declaration

for i in range(6):
    gp_s=cv2.pyrDown(Soap); #pyramid down of soap
    gp_e=cv2.pyrDown(Eva); #pyramid down of eva image

    gps.append(gp_s); # append value to list
    gpe.append(gp_e); #append value to list

#==>Create a lasplacian pyramid of image
lpS=[gps[5]]; #python list declaration
lpE=[gpe[5]]; #Python list declration

for i in range(5,0,-1):
    gp_E=cv2.pyrUp(gpe[i]); #pyramid up of image
    gp_S=cv2.pyrUp(gps[i]); #pyramid up of image

    print('This is for Gaussian pyramid of level 5 :'+str(gp_E[4]));
    print('This is for Gaussian pyrmid of level 4:'+str(gp_E[4]));

    L_S=cv2.subtract(gps[i-1],gp_S); #subtradct image
    L=cv2.subtract(gpe[i-1],gp_E); #subtract image
    lpE.append(L); #append value to list
    lpS.append(L_S); #append value to list

#add halve of images
Halves=[]; #python list decaration
for lp_s,lp_e in zip(lpS,lpE):
    rows,cols,channels=lp_s.shape;
    halve=np.hstack((lp_s[:,0:cols/2],lp_e[:,cols/2:])); #create a hstack of halves
    Halves.append(halve); #append value to list


blend_image=Halves[0]; #list declaration
for i in range(1,6):
    lp_=cv2.pyrUp(blend_image); #pyramid up of image
    blend_image=cv2.add(lp_,Halves[i]); #add images together

cv2.namedWindow('Blend',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Blend',blend_image); #image show
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow('Blend'); #destroy window




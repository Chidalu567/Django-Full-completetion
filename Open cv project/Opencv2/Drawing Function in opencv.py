'''We use the cv2.(line,rectangle,circle,ellipse,putText,polylines) functions to draw things in opencv2'''
import cv2
import numpy

img=numpy.zeros((512,512,3),numpy.uint8); #create a black background
#===>Drawing line in opencv
cv2.line(img,(0,0),(450,450),(255,255,0),3); #create a line in cv2

#===Drawing Rectangle in opencv
cv2.rectangle(img,(150,50),(400,20),(255,255,0),2); #create a rectangle

#===>Drawing circle
cv2.circle(img,(400,200),35,(255,255,0),2); #create a circle

#===>Drawing ellipse
cv2.ellipse(img,(300,200),(100,300),360,20,180,(255,255,0),2); #create an ellipse

#==>Putting Text
cv2.putText(img,'OPEN CV ',(100,200),cv2.FONT_HERSHEY_SIMPLEX,2,(225,225,0),2); #puttext in opencv

#Drawing of polylines
Vertices=numpy.array([[100,300],[50,200],[100,100],[200,100],[300,200],[200,300]],numpy.int32); #cretae an array
points=Vertices.reshape((-1,1,2)); #reshape array
cv2.polylines(img,[points],True,(255,255,0),4); #create a polyline

cv2.namedWindow('Draw Function',cv2.WINDOW_NORMAL); #create a named window
cv2.imshow('Draw Function',img); #show image
cv2.imwrite('Drawn by opencv.png', img); #write image
if cv2.waitKey(0)&0xFF==ord('q'):
    cv2.destroyWindow(); #destroy window

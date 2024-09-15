import cv2
from random import randrange as r

# Make sure the path to the XML file is correct
trainedData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:
    sucess,frame = webcam.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faceCoordinates = trainedData.detectMultiScale(gray)
    for x, y, w, h in faceCoordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (r( 0, 256),r(0,256),r(0,256)), 2)
        
    cv2.imshow('window',frame)
    
    k = cv2.waitKey(1) 
    if (k==81 or k==113):
        break
webcam.release()

print('end of program')
        
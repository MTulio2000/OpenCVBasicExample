import numpy as np
import cv2 as cv
#Capture object, to read webcam
vid = cv.VideoCapture(0)

#Loop for show video's frames
while True:
    #reading camera frame
    ret,frame = vid.read()
    #turns the frame to gray scale
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #turns the frame to edges, using Canny function
    edge = cv.Canny(frame,100,200)
    #inverting frame
    inverted = (255-frame)
    #show each channel
    (B, G, R) = cv.split(frame)
    cv.imshow("Blue",B)
    cv.imshow("Green",G)
    cv.imshow("Red",R)
    #show all merged channels
    cv.imshow("Merged",cv.merge([B,G,R]))
    #show all frames
    cv.imshow('frame',frame)
    cv.imshow('edge',edge)
    cv.imshow('inverted',inverted)
    #listening if have key event to quit main loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
#finishing video
vid.release()
#closing the windows
cv.destroyAllWindows()
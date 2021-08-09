import cv2
import numpy as np
import os
import time
import sys

from datasetconfig import get_counter
from json_operator import populate_name_array
from update_attendance import update

def sum_of_array(confidence_array):
    if __name__ == '__sum_of_array__':
        sum_of_array(confidence_array)

    i = 0
    for c in confidence_array:
        i = i+c
    return i

def image_recognizer():
    if __name__ == '__image_recognizer__':
        image_recognizer()

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('../model/trainer.yml')
    cascadePath = "../database/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    # Get ID index number
    id = 0

    # create a confidence_array
    confidence_array = []

    size_of_array = 0

    # Populate the names array
    names = ['None']
    names = populate_name_array(names)

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # setting a final limit for the timed loop
    end_time = time.time() + 5

    while time.time() < end_time:
        ret, img =cam.read()
        if ret==False:
            print("Error in Boolean Variable!!!")
            break
        #img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "{0}".format(round(100 - confidence))
            else:
                id = "Unknown"
                confidence = "{0}".format(round(100 - confidence))

            # Store all the confidence values recorder in an arraylist - in case of only if id is not Unknown
            if(id!="Unknown"):
                confidence_array.append(int(confidence))
            size_of_array = len(confidence_array)
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence + "%"), (x+5,y+h-5), font, 1, (255,255,0), 1)

        cv2.imshow('camera',img)

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    #Calculate mean confidence - then apply the below condition
    mean_confidence = sum_of_array(confidence_array)/size_of_array
    if(int(mean_confidence) >= 25):
        # put the code to update the attendance here - consider the situation where id = Unknown
        if(id!='Unknown'):
            update(id)

    # Do a bit of cleanup
    cam.release()
    cv2.destroyAllWindows()

image_recognizer()
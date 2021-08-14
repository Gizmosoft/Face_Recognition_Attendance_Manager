import cv2
import os
import time
import sys

from datasetconfig import get_and_update_counter
from json_operator import write_to_json_file

def data_gatherer():
    if __name__ == '__data_gatherer__':
        data_gatherer()

    # cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    face_detector = cv2.CascadeClassifier('../database/haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id - get the face id from get_counter()
    face_id = get_and_update_counter()
    username = input("Please enter the name of the person: ")
    # Store the user data into the json database
    datastorage_status = write_to_json_file(face_id, username)
    # Print and check if it ran to some error - this is a very bad way of checking the exception case but lol, who's gonna read my code!! :P
    if(datastorage_status == "There was some error storing the userdata!"):
        sys.exit(datastorage_status)
    print(datastorage_status)
    print("\n [INFO] Initializing face capture. Hi " + str(username) + ", look in the camera and wait ...")
    time.sleep(2)
    # Initialize individual sampling face count
    count = 0

    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("../dataset/" + str(username)+ '_' + str(face_id) + '_' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 50: # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

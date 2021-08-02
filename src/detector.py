import cv2
import numpy as np
import os

from datasetconfig import get_counter

def image_recognizer():
    if __name__ == '__image_recognizer__':
        image_recognizer()
        
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('../model/trainer.yml')
    cascadePath = "./database/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    # Get ID index number
    id = get_counter()

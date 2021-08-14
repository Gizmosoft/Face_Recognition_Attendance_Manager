import sys

from dataGathering import data_gatherer
from trainer import getImagesAndLabels, train_images
from detector import image_recognizer

def options():
    if __name__ == '__options__':
        options()

    print("Please select any one option below... (Press 1, 2 or 3)\n")
    print("1) Train a new face.\n2) Mark attendance.\n3) Quit program.\n")
    return input()

def driver():
    if __name__ == '__driver__':
        driver()

    print("Welcome to Face Recognition - Attendance Manager!\n")
    print("Please select any one option below")
    userinput = ""
    userinput = options()

    if(userinput=='1'):
        print("Please help us to gather your face data for our model to learn...\n")
        data_gatherer()
        print("Thank you for your cooperation. Our system is now reading the data you provided.\n")
        getImagesAndLabels()
        print("Our Machine Learning model is now trying to learn your face from the data...\n")
        train_images()
        print("Thank you for your patience. Your data has been captured and learnt successfully!\n")
        sys.exit()
    elif(userinput=='2'):
        print("Please look in to the camera while we try to mark your attendance...\n")
        image_recognizer()
        print("Kindly check the attendance_report.csv file for any updates. Thank you!!!\n")
        sys.exit()
    else:
        print("Thank you!")
        sys.exit()

driver()
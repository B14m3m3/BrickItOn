import cv2
from config import *


class Webcam:
    def __init__(self):
        print("Using webcam number", Config.webcam)

    def takePicture(self):
        cam = cv2.VideoCapture(Config.webcam)
        retval, frame = cam.read()
        if retval != True:
            raise ValueError("Can't read frame")

        # cv2.imwrite('img2.png', frame)
        cv2.imshow("img1", frame)
        cv2.waitKey()
        return frame


cam = Webcam();
cam.takePicture();
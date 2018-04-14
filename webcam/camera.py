import argparse
import cv2
from config import *


class Webcam:
    def __init__(self):
        self.cam = cv2.VideoCapture(Config.webcam)

    def takePicture(self):
        retval, frame = self.cam.read()
        if retval != True:
            raise ValueError("Can't read frame")
        return frame

if __name__ == "__main__":
    print("Testing if the camera module works")
    
    cam = Webcam()
    while True:
        frame = cam.takePicture()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

import argparse
import cv2
from config import *


class Webcam:
    def __init__(self, cameraNum):
        self.cam = cv2.VideoCapture(cameraNum)

    def takePicture(self):
        retval, frame = self.cam.read()
        if retval != True:
            raise ValueError("Can't read frame")
        return frame


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Test if camera works module")

    parser.add_argument('-c', '--camera', help='Use this if you have a integrated camera', action='store_true')

    args = parser.parse_args()
    
    cam = Webcam(1) if args.camera else Webcam(0)
    while True:
        cam.takePicture()

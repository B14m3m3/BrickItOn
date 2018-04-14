import webcam as wb
import numpy as np
import cv2


def picture_loop():
    cam = wb.Webcam(1)
    while True:
        frame = cam.takePicture()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        res_green = green_image(frame, hsv)
        res_red = red_image(frame, hsv)
        res_blue = blue_image(frame, hsv)

        cv2.imshow('frame',frame)
        cv2.imshow('res_green', res_green)
        cv2.imshow('res_blue', res_blue)
        cv2.imshow('res_red',res_red)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def green_image(frame, hsv):
    sensitivity = 15
    lower_green = np.array([40, 80, 50], dtype=np.uint8)
    upper_green = np.array([80, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    return res

def red_image(frame, hsv):
    lower_red = np.array([0, 80, 50], dtype=np.uint8)
    upper_red = np.array([10, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    return res

def blue_image(frame, hsv):
    # define range of blue color in HSV
    lower_blue = np.array([90,80,50])
    upper_blue = np.array([160,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    return res

if __name__ == '__main__':
    picture_loop()

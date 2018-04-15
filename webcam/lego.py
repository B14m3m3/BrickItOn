import camera as wb
import numpy as np
import cv2
import time
import Connector.Connector as con

value = (5,5)
connection = con.Connector()

def picture_loop():
    cam = wb.Webcam()
    while True:
        frame = cam.takePicture()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        res_red, mask_red = red_image(frame, hsv)
        res_blue, mask_blue = blue_image(frame, hsv)
        res_yellow, mask_yellow = yellow_image(frame, hsv)
        
        mask = mask_red + mask_blue + mask_yellow
        cv2.imshow('res_blue', mask_blue)
        cv2.imshow('res_red', mask_red)
        cv2.imshow('res_yellow', mask_yellow)
        cv2.imshow('comb', mask)
        
        
        edges_red = cv2.Canny(mask_red, 100, 150)
        edges_blue = cv2.Canny(mask_blue, 100, 150)
        edges_yellow = cv2.Canny(mask_yellow, 100, 150)
        _, contours_red, _ = cv2.findContours(edges_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        _, contours_blue, _ = cv2.findContours(edges_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        _, contours_yellow, _ = cv2.findContours(edges_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        contours = contours_red + contours_blue + contours_yellow
        
        if(len(contours) != 0):
            filtered_countours = [contour for contour in contours if cv2.contourArea(contour) > 75]
            cv2.drawContours(frame, filtered_countours, -1, (0,255,0), 1)
        
        cv2.imshow('frame',frame)


        pressed = cv2.waitKey(1)

        if pressed & 0xFF == ord('l'):
            if(len(contours) != 0):
                print("click")
                color_results = colors(hsv, filtered_countours)
                color_mapper(color_results)
            else:
                print("Error no contours")

        if pressed & 0xFF == ord('q'):
            break
        

def yellow_image(frame, hsv):
    lower_yellow = np.array([11, 80, 50], dtype=np.uint8)
    upper_yellow = np.array([39, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    gaus_mask = cv2.GaussianBlur(mask, value, 0)
    res = cv2.bitwise_and(frame, frame, mask=gaus_mask)
    return res, gaus_mask


def red_image(frame, hsv):
    lower_red = np.array([0, 80, 50], dtype=np.uint8)
    upper_red = np.array([10, 255, 255], dtype=np.uint8)
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([160, 80, 50], dtype=np.uint8)
    upper_red = np.array([179, 255, 255], dtype=np.uint8)
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    mask = cv2.addWeighted(mask0, 1.0, mask1, 1.0, 0.0)

    gaus_mask = cv2.GaussianBlur(mask, value, 0)
    res = cv2.bitwise_and(frame, frame, mask=gaus_mask)
    return res, gaus_mask

def blue_image(frame, hsv):
    lower_blue = np.array([90, 80, 50], dtype=np.uint8)
    upper_blue = np.array([160, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    gaus_mask = cv2.GaussianBlur(mask, value, 0)
    res = cv2.bitwise_and(frame, frame, mask=gaus_mask)
    return res, gaus_mask

def colors(hsv, contours):
    res = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x+w//2, y+h//2
        color = hsv[cy, cx, 0]
        value = hsv[cy, cx, 2]

        if color < 10 or color > 160:
            res.append([cx, cy, 'R'])
        elif 11 < color < 39:
            res.append([cx, cy, 'Y'])
        elif 90 < color < 160:
            res.append([cx, cy, 'B'])

    res = sorted(res, key=lambda res: res[1])
    return [x[2] for x in res]

def color_mapper(colors):
    for c in colors:
        if c is 'R':
            print("R")
            connection.forward()
        elif c is 'B':
            print("B")
            connection.turn_right()
        elif c is 'Y':
            print('Y')
            connection.turn_left()
        else:
            print("Error")
        
        time.sleep(0.5)
        

if __name__ == '__main__':
    picture_loop()

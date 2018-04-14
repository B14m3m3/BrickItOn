import webcam as wb
import numpy as np
import cv2




value = (5,5)


def picture_loop():
    cam = wb.Webcam()
    while True:
        frame = cam.takePicture()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        res_green, mask_green = green_image(frame, hsv)
        res_red, mask_red = red_image(frame, hsv)
        res_blue, mask_blue = blue_image(frame, hsv)
        
        
        full_mask = mask_green + mask_red #+ mask_blue
        #cv2.imshow('full_mask', full_mask)
        #cv2.imshow('res_green', res_green)
        #cv2.imshow('res_blue', res_blue)
        #cv2.imshow('res_red',res_red)
        
        
        res = cv2.bitwise_and(frame, frame, mask= full_mask)
        cv2.imshow('full_mask', res)
        
        edges = cv2.Canny(res, 180, 200)
        _, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        filtered_countours = [contour for contour in contours if cv2.contourArea(contour) > 150]
        cv2.drawContours(frame, filtered_countours, -1, (0,255,0), 2)
        cv2.imshow('frame',frame)

        pressed = cv2.waitKey(1)

        if pressed & 0xFF == ord('l'):
            color_resuts = colors(hsv, filtered_countours)

        if pressed & 0xFF == ord('q'):
            break

def green_image(frame, hsv):
    lower_green = np.array([50, 80, 50], dtype=np.uint8)
    upper_green = np.array([90, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    gaus_mask = cv2.GaussianBlur(mask, value, 0)
    res = cv2.bitwise_and(frame, frame, mask= gaus_mask)
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
    res = cv2.bitwise_and(frame, frame, mask= gaus_mask)
    return res, gaus_mask

def blue_image(frame, hsv):
    lower_blue = np.array([90, 40, 50], dtype=np.uint8)
    upper_blue = np.array([160, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    gaus_mask = cv2.GaussianBlur(mask, value, 0)
    res = cv2.bitwise_and(frame, frame, mask=gaus_mask)
    return res, gaus_mask

def colors(hsv, contours):
    res = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w//2, y+h//2
        color = hsv[cy,cx,0]

        if (color < 10 or color > 160):
            res.append([cx,cy,'R'])
        elif(50 < color < 90):
            res.append([cx,cy,'G'])
        elif(20 < color < 40):
            res.append([cx,cy,'Y'])
        elif(90 < color < 160):
            res.append([cx,cy,'B'])

    res = sorted(res,key = lambda res : res[0])
    return [x[2] for x in res]

def colorMapper(colors):
    for c in colors:
        if c is 'G':
            print("Forward")
        elif c is 'R':
            print("Stop")
        elif c is 'B':
            print("Left")
        elif c is 'Y':
            print("Right")
        else:
            print("Error")

if __name__ == '__main__':
    picture_loop()

import webcam.camera as wb
import numpy as np
import cv2
from webcam.feeder import *


class Hand(Feeder):
    def next(self):
        return self.picture_loop(False)

    def picture_loop(self, endless = True):
        cam = wb.Webcam()
        while True:
            frame = cam.takePicture()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            res_blue, mask_blue = self.blue_image(frame, hsv)
            cv2.imshow('blurred', res_blue)



            edges = cv2.Canny(res_blue, 100, 200)
            _, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            filtered_countours = [contour for contour in contours if cv2.contourArea(contour) > 150]

            cv2.drawContours(frame, filtered_countours, -1, (0, 255, 0), 1)
            cv2.imshow('filtered_contours', frame)

            pressed = cv2.waitKey(1)

            if pressed & 0xFF == ord('l'):
                print(self.colors(hsv, contours))
            if pressed & 0xFF == ord('p'):
                chopped = self.crop_img(frame, filtered_countours)

                if not endless:
                    return chopped
            if pressed & 0xFF == ord('q'):
                break

    def crop_img(self, img, contours):
        img_buffer = 30
        cnt = max(contours, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(cnt)
        crop_img = img[y-img_buffer:y+h+img_buffer, x-img_buffer:x+w+img_buffer]
        img_grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(img_grey,(28,28))
        cv2.imwrite('crop_img.png', img_grey)
        cv2.imwrite('crop_img_resized.png', resized_img)
        return resized_img

    def blue_image(self, frame, hsv):
        # define range of blue color in HSV
        lower_blue = np.array([80, 80, 50])
        upper_blue = np.array([100, 255, 255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        gaussian_mask = cv2.GaussianBlur(mask, (55, 55), 0)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=gaussian_mask)
        return res, gaussian_mask


    def colors(self, hsv, contours):
        res = []
        for cnt in contours:
            if cv2.contourArea(cnt) > 100:
                x, y, w, h = cv2.boundingRect(cnt)
                cx, cy = x + w // 2, y + h // 2
                color = hsv[cy, cx, 0]

                if (color < 10 or color > 170):
                    res.append([cx, cy, 'R'])
                elif (50 < color < 70):
                    res.append([cx, cy, 'G'])
                elif (20 < color < 40):
                    res.append([cx, cy, 'Y'])
                elif (110 < color < 130):
                    res.append([cx, cy, 'B'])

        res = sorted(res, key=lambda res: res[0])
        return [x[2] for x in res]


if __name__ == '__main__':
    feeder = Hand()
    feeder.picture_loop()

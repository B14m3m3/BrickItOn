import webcam.camera as wb
import numpy as np
from PIL import Image
import cv2
import sys
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

            cv2.imshow('mask', mask_blue)
            edges = cv2.Canny(res_blue, 100, 200)
            _, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            filtered_countours = [contour for contour in contours if cv2.contourArea(contour) > 150]
            filtered_countours2 = [cv2.convexHull(c) for c in filtered_countours]

            cv2.drawContours(frame, filtered_countours2, -1, (0, 255, 0), 1)
            # cv2.imshow('filtered_contours', frame)

            cv2.imshow('current ', frame)
            pressed = cv2.waitKey(1)

            if pressed & 0xFF == ord('p'):
                chopped = self.crop_img(frame, filtered_countours2)
                if not endless:
                    return chopped
            if pressed & 0xFF == ord('q'):
                break


    def crop_img(self, img, contour2):
        mask = np.zeros(img.shape, np.uint8)
        for c in contour2:
            (x, y, w, h) = cv2.boundingRect(c)
            crop = img[y:y + h, x:x + w]
            #cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 0, 255), -1)
        #res = cv2.bitwise_and(img, mask)

        img_grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        x, y = img_grey.shape[:2]
        size = 28
        #resized = cv2.resize(img_grey, (28,28), interpolation=cv2.INTER_AREA)
        #a, b = img.shape[:2]
        #aspect = b/a
        #new_im = Image.new('RGBA', (28, 28), (0,0,0,0))
        #new_im.paste(img_grey, ((size-x)/2,(size-y)/2))
        new_im = self.resizeAndPad(img_grey, (28, 28), padColor=255)

        # currentHeight, currentWidth = img_grey.shape[:2]
        # aspectRatio = currentWidth / currentHeight
        # area = currentHeight * currentWidth
        #
        # resized_img = cv2.resize(img_grey, (28, 28))
        # height, width = resized_img.shape[:2]
        #

        cv2.imwrite('crop_img.png', img_grey)
        cv2.imwrite('crop_img_resized.png', new_im)

        return new_im

    def resizeAndPad(self, img, size, padColor=0):

        h, w = img.shape[:2]
        sh, sw = size

        # interpolation method
        if h > sh or w > sw:  # shrinking image
            interp = cv2.INTER_AREA
        else:  # stretching image
            interp = cv2.INTER_CUBIC

        # aspect ratio of image
        aspect = w / h  # if on Python 2, you might need to cast as a float: float(w)/h

        # compute scaling and pad sizing
        if aspect > 1:  # horizontal image
            new_w = sw
            new_h = np.round(new_w / aspect).astype(int)
            pad_vert = (sh - new_h) / 2
            pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
            pad_left, pad_right = 0, 0
        elif aspect < 1:  # vertical image
            new_h = sh
            new_w = np.round(new_h * aspect).astype(int)
            pad_horz = (sw - new_w) / 2
            pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
            pad_top, pad_bot = 0, 0
        else:  # square image
            new_h, new_w = sh, sw
            pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

        # set pad color
        if len(img.shape) is 3 and not isinstance(padColor,
                                                  (list, tuple, np.ndarray)):  # color image but only one color provided
            padColor = [padColor] * 3

        # scale and pad
        scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
        scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right,
                                        borderType=cv2.BORDER_CONSTANT, value=padColor)

        return scaled_img
    def blue_image(self, frame, hsv):
        # define range of blue color in HSV
        lower_blue = np.array([70, 80, 50])
        upper_blue = np.array([110, 255, 255])
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

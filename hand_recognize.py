import numpy as np
import math
import cv2 as cv

cap = cv.VideoCapture(0)


while True:

    _, img = cap.read()
    cv.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 0)
    crop_img = img[100:300, 100:300]
    grey = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred_ = cv.GaussianBlur(grey, value, 0)
    _, thresholded = cv.threshold(blurred_, 127, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    image, contours, hierarchy = cv.findContours(thresholded.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    count1 = max(contours, key=lambda x: cv.contourArea(x))
    x, y, w, h = cv.boundingRect(count1)
    cv.rectangle(crop_img, (x, y), (x + w, y + h), (0, 0, 255), 0)
    hull = cv.convexHull(count1)
    drawing = np.zeros(crop_img.shape, np.uint8)
    cv.drawContours(drawing, [count1], 0, (0, 255, 0), 0)
    cv.drawContours(drawing, [hull], 0, (0, 0, 255), 0)
    hull = cv.convexHull(count1, returnPoints=False)
    defects = cv.convexityDefects(count1, hull)
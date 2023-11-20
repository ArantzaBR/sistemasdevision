# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:11:45 2023

@author: bazal
"""


import cv2

img0 = cv2.imread('pacman.jpg')

scale_percent = 30 # Porcentaje de la imagen original
width = int(img0.shape[1] * scale_percent / 100)
height = int(img0.shape[0] * scale_percent / 100)
dim = (width, height)

image = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)


template = cv2.imread('pm.png')

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

x1, y1 = min_loc
x2, y2 = min_loc[0] + template.shape[1], min_loc[1] + template.shape[0]
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("Image", image)
cv2.imshow("Template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()
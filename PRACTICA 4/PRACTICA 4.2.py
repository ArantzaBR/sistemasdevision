# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:32:08 2023

@author: bazal
"""
import cv2
import numpy as np

# Read the main image
img0 = cv2.imread('pacman.jpg')

scale_percent = 30 # Porcentaje de la imagen original
width = int(img0.shape[1] * scale_percent / 100)
height = int(img0.shape[0] * scale_percent / 100)
dim = (width, height)

img_rgb = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)
  
# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  
# Read the template
template = cv2.imread('pm.png', 0)
  
# Store width and height of template in w and h
w, h = template.shape[::-1]
  
# Perform match operations.
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
  
# Specify a threshold
threshold = 0.8
  
# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)
  
# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
  
# Show the final image with the matched area.
cv2.imshow('Detected', img_rgb)
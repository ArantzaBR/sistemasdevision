# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:44:41 2023

@author: bazal
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the two images
input_img = cv2.imread('pacman.jpg')
img2 = cv2.imread('pm.png')

# Convert the images to grayscale
input_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Find the dimensions of the template image
w, h = template_gray.shape[::-1]

# Use the cv2.matchTemplate() function to find the correlation between the images
result = cv2.matchTemplate(input_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Set the threshold for the correlation coefficient
threshold = 0.30
loc = np.where(result >= threshold)

# Check if there are any good matches
if len(loc[0]) > 0:
    # Draw a rectangle around each good match
    for pt in zip(*loc[::-1]):
        cv2.rectangle(input_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    print("Good match found.")
else:
    print("No good match found.")

# Find the location of the maximum value in the result image
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the maximum value in the result image
top_left = max_loc
bottom_right = (top_left[0] + img2.shape[1], top_left[1] + img2.shape[0])
img_matches = cv2.rectangle(input_img, top_left, bottom_right, 255, 2)

# Display the results
plt.figure(figsize = (20,10))
plt.imshow(img_matches)


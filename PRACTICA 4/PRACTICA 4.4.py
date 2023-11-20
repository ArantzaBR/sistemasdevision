# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:49:35 2023

@author: bazal
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the two images
input_img = cv2.imread('pacman.jpg')
template_img = cv2.imread('pm.png')

# Convert the images to grayscale
input_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)

# Detect ORB keypoints and descriptors in the images
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(input_gray, None)
keypoints2, descriptors2 = orb.detectAndCompute(template_gray, None)

# Use the BFMatcher to find the best matches between the descriptors
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

# Sort the matches based on their distances
matches = sorted(matches, key = lambda x:x.distance)

# Draw the matches on the images
img_matches = cv2.drawMatches(input_img, keypoints1, template_img, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the results
plt.figure(figsize = (20,10))
plt.imshow(img_matches)
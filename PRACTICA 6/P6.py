# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:23:33 2023

@author: bazal
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Definimos la funcion que muestra imagenes
def imshow(title = "Image" , image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize = (size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
    
image = np.zeros((512,512,3), dtype = np.uint8)
image[:,:,:] = (250,235,215)


cv2.line(image,(400,100),(500,200),(255,127,80), 9)

cv2.rectangle(image,(220,200),(350,300),(127,50,127), 9)

cv2.circle(image,(150,100),50,(95,158, 160),8)

ourString = "Arantza"
cv2.putText(image, ourString, (50,450),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,4,(40,0,0),2)

pts = np.array([[10,120],[200,220],[90,200],[100,350]],np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, (70, 130, 180),3)

imshow("Canvas - RGB Color", image)



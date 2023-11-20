# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:27:45 2023

@author: bazal
"""

import cv2
import numpy as np


# Cargar imagen
img0 = cv2.imread('Mariposas.jpg')

scale_percent = 20 # Porcentaje de la imagen original
width = int(img0.shape[1] * scale_percent / 100)
height = int(img0.shape[0] * scale_percent / 100)
dim = (width, height)


fin = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)

#Se convierte a grises
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

#Se redimensiona la imagen
scale_percent = 20 # Porcentaje de la imagen original
width = int(gray.shape[1] * scale_percent / 100)
height = int(gray.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

#Normalizando los pixeles de la imagen
norm_img = cv2.normalize(img, None, 20, 230 , cv2.NORM_MINMAX)
cv2.imshow("Norm",norm_img)


#Se agrega mascara de imagen
Mask = cv2.Laplacian(norm_img,cv2.CV_64F)
Mask1 = cv2.convertScaleAbs(Mask)

#Se identifican los bordes
bordes = cv2.Canny(img,100,200)

contours, hierarchy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

foto = cv2.drawContours(fin, contours, -1, (0, 150, 0), 1)
cv2.imshow('Contours', foto)

cv2.waitKey(0)
cv2.destroyAllWindows()



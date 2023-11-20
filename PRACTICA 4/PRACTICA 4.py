# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:55:36 2023

@author: bazal
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Leer la imagen principal
img0 = cv2.imread('pacman.png')

scale_percent = 150 # Porcentaje de la imagen original
width = int(img0.shape[1] * scale_percent / 100)
height = int(img0.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)


cv2.imshow('pacman',img)

#Convertir a escala gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Test',gray)

#Leer la plantilla
template = cv2.imread('pm.png')


#Almacenar la anchura (w) y la altura (h) de la plantilla
w, h = template.shape[::-1]

#Realizar operaciones de coincidencia
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

#Especificar un umbral (threshold)
threshold = 0.5

#Almacenar las coordenadas del área coincidente en un array numpy
loc = np.where( res >= threshold)

#Dibujar un rectángulo alrededor de la región adaptada encontrada
for pt in zip(*loc[:,:,-1]):
    cv2.rectangle[img, pt, (pt+ w, pt+h),(0,255,255), 1]

#Mostrar la imagen final con el área correspondiente
cv2.imshow('pacman',template)
cv2.imshow('Detectado',img)
cv2.waitKey(0)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:27:45 2023

@author: bazal
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar imagen
img0 = cv2.imread('RELOJ.jpg')

# Convertir a gris
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

scale_percent = 60 # Porcentaje de la imagen original
width = int(gray.shape[1] * scale_percent / 100)
height = int(gray.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

#Binarización de la imagen
_ , imgBin = cv2.threshold(img, 120 ,255, cv2.THRESH_BINARY)

#Se muestran las matrices de los filtros
k1 = np.array([[-1,1],[1,0]])
k2 = np.array([[-3,2,-0.5],[2,0,0],[-0.5,0,0]])
k3 = np.array([[-8/3,3/2,0,-1/6],[3/2,0,0,0],[0,0,0,0],[-1/6,0,0,0]])

#Se utiliza el comando que llamara a los filtros
R1 = cv2.filter2D(imgBin,-1, k1)
R2 = cv2.filter2D(imgBin,-1,k2)
R3 = cv2.filter2D(imgBin,-1,k3)



#Se muestran las imagenes
plt.subplot(2,3,1), plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2), plt.imshow(R1,cmap = 'gray')
plt.title('Filtro 1'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3), plt.imshow(R2,cmap = 'gray')
plt.title('Filtro 2'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,4),plt.imshow(R3,cmap = 'gray')
plt.title('Filtro 3'), plt.xticks([]), plt.yticks([])



plt.show()

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:11:37 2023

@author: bazal
"""

import cv2
import numpy as np

#Se adquire y lee la imagen
img = cv2.imread('imagen1.jpeg')

#Se redimensiona la imagen
res = cv2.resize(img, (600,400), interpolation=cv2.INTER_LINEAR)
cv2.imshow("res", res)

#Se hace una normalización de los pixeles de la imagen
norm_img1 = np.zeros((600,400))
norm_img = cv2.normalize(res, norm_img1, 0, 100 , cv2.NORM_MINMAX)

#Se muestra el preprocesamiento de la imagen
cv2.imshow("Norm",norm_img)


cv2.waitKey(0)
cv2.destroyAllWindows()

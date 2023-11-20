#Importamos librerias y creamos la funcion Imshow para mostrar imagenes
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Definimos nuestra función para mostrar imagenes
def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

#Creamos un fondo negro utilizando numpy para crear nuestro arreglo
image = np.zeros((512,512,3), np.uint8)



#Mostramos nuestro canvas negro
#imshow("Black Canvas - RGB Color", image)

#Linea -------------------------------------------------------

cv2.line(image, (100,100), (370,420), (0,0,100), 5)


#Rectangulo -----------------------------------------------------

# Grosor 
cv2.rectangle(image, (100,100), (300,400), (127,50,127), 10)

#Circulo ----------------------------------------------------------

#Creamos nuestro circulo
cv2.circle(image, (250, 250), 150, (15,150,50), 20) 


#Poligono ---------------------------------------------------------

# Definimos nuestros puntos
pts = np.array( [[10,120], [400,600], [150,200], [120,500]], np.int32)
# Cambiamos la forma de nuestros puntos a la forma requerida por la funcion
pts = pts.reshape((-1,1,2))
cv2.polylines(image, [pts], True , (0,0,255), 3)


#Texto sobre imagen -------------------------------------------------

ourString =  'JASSO'
cv2.putText(image, ourString, (300,100), cv2.FONT_HERSHEY_PLAIN, 4, (40,200,0), 4)


#Mostramos imagen final -----------------------------------------------
imshow("Imagen con texto", image)
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


#Hay que tener cuidado al usar esta operación ya que a diferencia de otras operaciones de opencv
#esta no regresra una imagen nueva como respuesta si no que modificara nuestra imagen actual
#Recordar que nuestra imagen actual es el canvas negro
cv2.line(image, (100,100), (370,420), (0,0,255), 9)

#Mostramos nuestra imagen con linea
#imshow("Canvas negro con linea dibujada", image)


#Rectangulo -----------------------------------------------------
#Creamos nuestro canvas negro
#image = np.zeros((512,512,3), np.uint8)

# Grosor 
cv2.rectangle(image, (100,100), (300,250), (127,50,127), 10)

#imshow("Rectangulos en canvas negro", image)

#Circulo ----------------------------------------------------------
#Generamos nuestro canvas negro
#image = np.zeros((512,512,3), np.uint8)
#Creamos nuestro circulo
cv2.circle(image, (250, 250), 150, (15,150,50), 1) 
#imshow("Circulo en canvas negro", image)



#Poligono ---------------------------------------------------------


#image = np.zeros((512,512,3), np.uint8)

# Definimos nuestros puntos
pts = np.array( [[10,120], [400,300], [90,200], [120,500]], np.int32)

# Cambiamos la forma de nuestros puntos a la forma requerida por la funcion
pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True , (0,0,255), 3)
#imshow("Polygono en canvas negro", image)

#Texto sobre imagen -------------------------------------------------

#Generamos nuestra imagen
#image = np.zeros((1000,1000,3), np.uint8)
#Escribimos el texto que queramos que aparezca en la imagen
ourString =  'JASSO'
#Utilizamos la función
cv2.putText(image, ourString, (155,290), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (40,200,0), 4)
#Mostramos el resultado
imshow("Imagen con texto", image)
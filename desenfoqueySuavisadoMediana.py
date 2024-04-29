import cv2 as cv
import numpy as np

img = cv.imread("images/perro.jpg") 

# Muestra la imagen original
cv.imshow("imagen original", img)

# Aplica desenfoque Mediana, que es aun mejor que el gaussiano y el desenfoque blur
#es el preferido para usar en proyectos qure requieran una reduccion significativa de ruido
median=cv.medianBlur(img,3)#aqui no se usa una matriz de 3 x 3 en el grano el asume una matriz cuadrada asi que el parametro solo recive un numero entero

cv.imshow("desenfoque con Mediana", median)

cv.waitKey(0)
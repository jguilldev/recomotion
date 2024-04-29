import cv2 as cv 
import numpy as np


img = cv.imread("images/perro.jpg") #guarda la imagen en una variable
cv.imshow("imagen original",img)# muestra la imagen

#el desenfoque se usa para reducir el ruido en la imagen

#exxisten mas tipos de desenfoque que el gausiano
#window se le llama a la seccion de desenfoque las medidas de la ventana se llaman grain size (tamaño del grano)
# el desenfoque se aplica a la mitad del tamaño del grano es deir al que esta en todo el centro de la matriz (pixel intensidad sera el promedio de la intensidad de pixeles) por llamarlo de alguna forma. El tamaño de la ventana se desliza y repite el proceso en la siguiente parte de la imagen

average=cv.blur(img, (3,3))#el 3x3 se rrefiere en este argumento a la ventana
# a mayor ventana mayor desenfoque
cv.imshow("desenfoque con blur",average)

cv.waitKey(0)#espera a que se oprima cualquier tecla para cerrar el programa 
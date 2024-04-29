import cv2 as cv
import numpy as np

img = cv.imread("images/perro.jpg") 

# Muestra la imagen original
cv.imshow("imagen original", img)

# Aplica desenfoque Gaussiano para reducir ruido  
#  con desenfoque gaussiano. El centro se ve nítido, y se va "desenfocando" conforme te alejas del centro.
gauss = cv.GaussianBlur(img, (7,7), 0)

# El tercer parámetro es sigmaX y define cuanto se extenderá 
# la distribución gaussiana en la dirección X.
# sigmaX=0 → se calcula automáticamente.
# sigmaX>0 → desviación estándar en X. Mayor valor, más difuminado.
# SigmaY se toma igual a sigmaX por defecto.

cv.imshow("desenfoque Gaussiano", gauss)

cv.waitKey(0)
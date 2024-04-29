import cv2 as cv
import numpy as np

img = cv.imread("images/perro.jpg") 

# Muestra la imagen original
cv.imshow("imagen original", img)

# Aplica desenfoque es el mas utilizado en proyectos de vision por computadora, este tipo de desenfoque retiene los bordes

bilateral=cv.bilateralFilter(img,5,15,15)
#  Parámetros:
# - Primero: Diámetro del filtro en píxeles
# - Segundo: Desviación estándar en espacio (pixeles vecinos) 
# - Tercero: Desviación estándar en colores (rangos de color)

# El primer parámetro define qué tan lejos pueden estar los píxeles vecinos para mezclarse con el pixel central. 

# El segundo parámetro Entre más grueso, más se extenderá sobre la imagen es el grosor. Si es 15, los pixeles hasta 15 unidades alrededor se combinarán.

# El tercer parámetro diferencia de colores. Define qué tan diferentes en color pueden ser los píxeles que se combinan
# Entre más alto el número, se combinarán pixeles con rangos de color más amplios. Si es bajo, solo mezcla colores muy similares.

cv.imshow("desenfoque con bilateral", bilateral)

cv.waitKey(0)
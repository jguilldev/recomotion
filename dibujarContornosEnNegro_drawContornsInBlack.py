#Bordes: Cambios rápidos en pixeles. Detectan transiciones en imagen.
#Contornos: Líneas alrededor de regiones. Identifican forma de objetos.
#Usos: Contornos para identificar objetos.


#los dos comentarios siguientes permiten entender la linea 32
# En cv.CHAIN_APPROX_NONE, se almacenan todos los puntos de contorno sin aproximar.
# Contornos son puntos que forman la forma de un objeto en imagen.
# Almacenar todos los puntos puede ser detallado pero usa más memoria.
# Usado cuando precisión es crucial y datos no son problema.


# La relación jerárquica es una noción que se aplica cuando se encuentran contornos en una imagen. Los contornos pueden estar organizados en una estructura jerárquica, lo que significa que algunos contornos pueden estar dentro de otros, creando una relación de "padre" e "hijo". Esta relación es útil cuando se trabaja con objetos anidados o estructuras complejas en una imagen.

import cv2 as cv
import numpy as np # se necesita numpy

#lee la imagen original
img =cv.imread("images/smiley.jpg")
cv.imshow("smile", img)

#generamos imagen en blanco
blank =np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank) # no es necesario llamarla ya que no pinta nada solo mostrara el fondo negro para usar con la funcion mas adelante.

#pasa la imagen a grises
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("En grises", gray)

#pasa la imagen a blancos y negros para que hayan menos puntos que reconocer
ret, thresh = cv.threshold( gray,125,255,cv.THRESH_BINARY ) # descomentar adelante si en vez de gray se usa canny
# 125 es el umbral
cv.imshow("Thresh",thresh)

# canny=cv.canny(img,125,175)
# cv.imshow("Canny edges",canny)
#estas tres lineas se descomentan si en la linea anterior numero 31 en vez de gray usamos canny

#pixel por debajo de 125 esta reconocido como negro
#pixel por encima de 125 esta reconocido como blanco

#Escoge muchos o minimos puntos
contours, hierarchies=cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#PRIMER ARGUMENTO
# Modos de recuperación de contornos en cv.findContours():
# - cv.RETR_LIST: Todos los contornos sin jerarquía.
# - cv.RETR_EXTERNAL: Solo contornos externos.
# - cv.RETR_CCOMP: Jerarquía de contornos externos e internos.
# - cv.RETR_TREE: Estructura jerárquica completa.

#SEGUNDO ARGUMENTO
# - cv.CHAIN_APPROX_NONE: Almacena todos los puntos del contorno.
# - cv.CHAIN_APPROX_SIMPLE: Aproxima contornos eliminando puntos redundantes.
print(f'{len(contours)} countour(s) found!')
#la linea anterior escribe en la consola los puntos encontrados en el contorno

cv.drawContours( blank, contours, -1,(0,0,255),2)
# blank: La imagen donde se dibujarán los contornos detectados. 
# Normalmente una imagen en blanco o negra.

# contours: La lista de contornos encontrados con cv.findContours().
# Cada contorno es una curva que representa el borde de un objeto.

# -1: Indica que se dibujarán todos los contornos de la lista. 
# Si pasamos un índice, solo dibuja ese contorno.

# (0,0,255): El color BGR con el que se dibujarán los contornos.
# En este caso rojo puro.  

# 2: El grosor de la línea en pixeles para dibujar cada contorno.
# Entre más grande, más gruesa la línea.


#EXPLICACION DEL -1
#  -1: Dibuja todos los contornos encontrados
#  Índice (0, 1, 2, etc.): Dibuja ese contorno por su índice
#  cv2.contourIdx.ALL: Equivale a -1, dibuja todos
#  cv2.contourIdx.FIRST: Dibuja solo el primer contorno 
#  cv2.contourIdx.LAST: Dibuja solo el último contorno
#  cv2.contourIdx.CHILDREN: Dibuja contornos hijos del principal


cv.imshow("contorno pintado en blank", blank)

cv.waitKey(0)

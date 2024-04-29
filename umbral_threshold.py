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

#lee la imagen original
img =cv.imread("images/smiley.jpg")
cv.imshow("smile", img)

#pasa la imagen a grises
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("En grises", gray)

#pasa la imagen a blancos y negros para que hayan menos puntos que reconocer
ret, thresh = cv.threshold( gray,125,255,cv.THRESH_BINARY ) #125 es el umbral
cv.imshow("Thresh",thresh)

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

cv.waitKey(0)
cv.destroyAllWindows()
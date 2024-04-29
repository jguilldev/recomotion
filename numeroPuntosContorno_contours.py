#Bordes: Cambios rápidos en pixeles. Detectan transiciones en imagen.
#Contornos: Líneas alrededor de regiones. Identifican forma de objetos.
#Usos: Contornos para identificar objetos.


#los dos comentarios siguientes permiten entender la linea 30
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

#si la imagen tiene muchos borde o contornos seria util usar un desenfoque aqui
# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)
#pero seria necesario cambiar el argumento de la imagen en el siguiente canny y asi consecutivamente

#encuentra bordes
canny= cv.Canny (img, 125,175)
cv.imshow("Canny bordes", canny)

#Escoge muchos o minimos puntos
contours, hierarchies=cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

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
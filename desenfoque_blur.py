# blur es desenfocar la imagen esto se hace para eliminar ruido
import cv2 as cv

img =cv.imread("images/smiley.jpg")
# cv.imshow("smile", img)
#la linea anterior solo dibuja la imagen original por eso esta comentada
cv.waitKey(0)

#funcion para convertir la imagen a un difuminado
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# - (3, 3): El tamaño del kernel del filtro. En este caso, es una matriz de 3x3, lo que significa que el filtro se aplicará a bloques de 3x3 píxeles.

cv.imshow("desenfoque", blur)

cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

# rotation permite establecer un punto de la matriz como eje de rotacion
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    #Índice 0: Representa el alto de la imagen.
#Índice 1: Representa el ancho de la imagen.
#Índice 2: Representa los canales de la imagen (solo aplicable en imágenes a color).

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
        #si no se define rotPoint se define el punto de rotacion la mitad de la imagen, por eso se divide por 2
        # un doble slash // es division con resultado entero

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    #cv.getRotationMatrix2D(). Los parámetros que recibe son:
#rotPoint: El punto de rotación alrededor del cual se realizará la rotación. En este caso, es el punto que se pasó como argumento a la función rotation o, si no se proporcionó, el punto central de la imagen (ancho // 2, alto // 2).
#angle: El ángulo en grados de la rotación que se aplicará a la imagen.
#scale: El factor de escala que se aplicará después de la rotación. En este caso, se usa 1.0 para no cambiar la escala.
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# Llamar a la función de rotación y mostrar la imagen rotada
rotated = rotation(img, 45)#para especificar giros en contra de las manecillas del reloj se usan angulos negativos
cv.imshow("rotated", rotated)
cv.waitKey(0)

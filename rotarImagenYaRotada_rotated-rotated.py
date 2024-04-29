import cv2 as cv
import numpy as np

img = cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

# La función rotation permite establecer un punto de la matriz como eje de rotación
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Obtener la matriz de transformación de rotación
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Definir las dimensiones de la imagen resultante
    dimensions = (width, height)

    # Aplicar la transformación de rotación a la imagen
    return cv.warpAffine(img, rotMat, dimensions)

# Llamar a la función de rotación y mostrar la imagen rotada
rotated = rotation(img, -45)  # Girar la imagen -45 grados (sentido contrario a las manecillas del reloj)
cv.imshow("rotated", rotated)

# Llamar a la función de rotación nuevamente para la imagen ya girada
rotated_rotated = rotation(rotated, -45)  # Girar la imagen -45 grados nuevamente
cv.imshow("rotado en sentido contrario a las manecillas", rotated_rotated)
#como la imagen anterior presentaba triangulos negros, la nueva imagen de la segunda rotacion los toma como si fueran parte de la imagen original, para el giro completo de la imagen original solo se deberian sumar los angulos y usar el codigo rotated.

cv.waitKey(0)

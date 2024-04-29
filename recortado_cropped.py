import cv2 as cv
import numpy as np

img = cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

cropped= img[200:400,300:400]
#se trae un recorte Cuando se trabaja con imágenes en OpenCV, puedes cortar o recortar una región específica de la imagen utilizando rebanadas de matriz. En este contexto, la imagen se trata como una matriz NumPy y puedes acceder a sus elementos utilizando índices y rebanadas.
# 200:400 define el rango vertical de las filas desde la fila 200 hasta la fila 399 (la fila 400 no está incluida).
#3 00:400 define el rango horizontal de las columnas desde la columna 300 hasta la columna 399 (la columna 400 no está incluida).

cv.imshow("cortada", cropped)

cv.waitKey(0)
cv.destroyAllWindows()
#como BGR es la imagen dada por defecto aveces se hara necesario invertirl por ejemplo matplotlib, usa un sistema RGB, por lo tanto los rojos se vuelven azules y azules rojos

import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread("images/smiley.jpg")
 #BGR es la forma predeterminada de mostrar la imagen
cv.imshow("smile", img)

# plt.imshow(img)  #RGB es la forma predeterminada de mostrar la imagen en matplotlib
# plt.show()

#de BGR a RGB
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

#las siguientes lineas muestran la imagen invertida en matplotlib
# es decir con los colores correctamente  
plt.imshow(rgb)
plt.show()
# matplotlibtrae de nuevo la imagen a color (con coordenadas)

# NO SE PUEDE CONVERTIR UNA IMAGEN EN ESCALA DE GRISES A HSB DE FORMA DIRECTA

# DEBERIAS CONVERTIR DE ESCALA DE GRISES A BGR Y LUEGO A HSV


cv.waitKey(0)
import cv2 as cv
import numpy as np

#crear forma desde 0, crea una ventana con las medidas
blank= np.zeros((500,500,3), dtype="uint8")# 3 es el numero de color
# cv.imshow("enBlanco",blank)

# pintar la imagen de cierto color
# blank[:]=0,0,255 #Aqui se le da el color en RGB
# cv.imshow("red",blank) #el primer argumento es el nombre de la ventana

# #pintar cierta parte de la imagen de cierto color
# blank[200:300, 300:400]=0,0,255# [200:300, 300:400] son pares ordenados o coordenadas dentro de la imagen
# cv.imshow("blue",blank)

#pintar un rectangulo
cv.rectangle(blank,(0,0), (250,250),(255,0,0,)) #coordenada de inicio, cordenada final, y color (en este caso rojo)
cv.imshow("rectangulo",blank)

cv.waitKey(0)



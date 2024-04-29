import cv2 as cv
import numpy as np

# para dibujar un rectangulo lleno
blank= np.zeros((500,500,3), dtype="uint8")# 3 es el numero de color

cv.putText(blank,"Hola",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),2)
#  se maneja un string "hola"
#(225,225 indica el punto de inicio
#cv.FONT_HERSHEY_TRIPLEX indica el tipo de fuente
#1.0 indica la escala de la fuente
# indica color (0,255,255)
# e indica espesor 2

cv.imshow("Line",blank)
cv.waitKey(0)
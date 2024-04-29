import cv2 as cv
import numpy as np

# para dibujar un rectangulo lleno
blank= np.zeros((500,500,3), dtype="uint8")# 3 es el numero de color

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255), thickness=3)
#indica el par ordenado de inicio
# (blank.shape[1]//2,blank.shape[0]//2) indica el final o par ordenado del final en este caso con arreglos para que sea exactamente la mitad
#,(255,255,255) indica el color en RGB en este caso blanco
#thickness=3 indica el color de la linea


cv.imshow("Line",blank)
cv.waitKey(0)
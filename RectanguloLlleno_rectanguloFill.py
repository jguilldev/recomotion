import cv2 as cv
import numpy as np

# para dibujar un rectangulo lleno
blank= np.zeros((500,500,3), dtype="uint8")# 3 es el numero de color

cv.rectangle(blank,(0,0), (250,500),(255,0,0), thickness=cv.FILLED) 
#si cambiamos de 250 a 500 asi:
#cv.rectangle(blank,(0,0), (250,500),(255,0,0), thickness=cv.FILLED) 
#la ventana ocupara todo el alto

# #coordenada de inicio, cordenada final, y color (en este caso rojo)
#reemplazando thickness=-1 la mitad de la ventana se rellenara de azul
#reemplazando thickness=cv.FILLED la mitad de la ventana se rellenara de azul

cv.imshow("rectangulo",blank)

cv.waitKey(0)
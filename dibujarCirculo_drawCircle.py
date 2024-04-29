import cv2 as cv
import numpy as np

# para dibujar un rectangulo lleno
blank= np.zeros((500,500,3), dtype="uint8")# 3 es el numero de color

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255), thickness=3)
#(blank.shape[1]//2,blank.shape[0]//2) hace que la ubicacion inicial sea el centro de la ventana
#,40 indica el numero de pixeles que tomara de radio
#indica el color en RGB
#indica el grosor de la linea
#thickness=-1 si usamos -1 el circulo se rellenara del color escogido en el RGB


cv.imshow("circle",blank)

cv.waitKey(0)
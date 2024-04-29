import cv2 as cv
import numpy as np

# para dibujar un rectangulo lleno
blank= np.zeros((500,500,3), dtype="uint8")# 3 es el numero de color

cv.rectangle(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2),(255,0,0), thickness=cv.FILLED) 
#en la linea anterior con blank.shape[1] nos referimos al ancho y le decimos que sea la mitad
#> lo mismo pasa con el alto al que nos referimos con [0]

cv.imshow("rectangulo",blank)

cv.waitKey(0)
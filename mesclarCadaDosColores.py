import cv2 as cv 
import numpy as np

# Leer imagen en OpenCV (BGR por defecto)
img = cv.imread("images/smiley.jpg")

# Crear imagen en blanco para canales
blank = np.zeros(img.shape[:2], dtype='uint8') 

# Separar canales BGR 
b, g, r = cv.split(img)

# Crear imagen solo con canal azul (en posición BGR correcta)
blue = cv.merge((b,blank,blank)) 

# Crear imagen solo con canal verde
green = cv.merge((blank,g,blank))  

# Crear imagen solo con canal rojo 
red = cv.merge((blank,blank,r))

# Mostrar imagen original 
cv.imshow('Original', img)

# Mostrar canales individuales  
cv.imshow('Azul', blue)
cv.imshow('Verde', green)
cv.imshow('Rojo', red)

# Fusionar canales BGR
merged = cv.merge((b,g,r))  

# Mostrar imagen fusionada
cv.imshow('Fusionada', merged)  

# Esperar tecla y cerrar ventanas
cv.waitKey(0)
cv.destroyAllWindows()
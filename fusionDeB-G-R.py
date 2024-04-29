import cv2 as cv
import matplotlib.pyplot as plt

# Lee la imagen en OpenCV (por defecto en BGR)
img = cv.imread("images/smiley.jpg")

# Muestra la imagen original 
cv.imshow("imagen", img)

# Divide la imagen en canales BGR
b, g, r = cv.split(img) 

# Muestra cada canal
cv.imshow("azul", b)
cv.imshow("verde", g) 
cv.imshow("rojo", r)

# Imprime dimensiones de imagen y canales
print("Dimensiones de la imagen original:", img.shape)
print("Dimensiones del canal azul (B):", b.shape)
print("Dimensiones del canal verde (G):", g.shape) 
print("Dimensiones del canal rojo (R):", r.shape)

# Fusiona los canales en orden BGR para OpenCV
merged = cv.merge((b, g, r))

# Muestra la imagen fusionada 
cv.imshow("fusionadas_BGR", merged)

# Espera hasta que se presione una tecla
cv.waitKey(0) 

# Cierra todas las ventanas
cv.destroyAllWindows()
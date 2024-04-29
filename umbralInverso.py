import cv2 as cv

img=cv.imread("images/perro.jpg")
cv.imshow("imagen original", img )

#en el umbral (tresholding) inverso lo que se hace es invertir el valor por encima del punto de referencia seran ceros, y por debajo del punto de referencia seran unos.

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# Umbral simple 
threshold, thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow("Umbral Inverso",thresh_inv)
# gray: Este es el primer argumento y representa la imagen en escala de grises en la que se aplicará la umbralización.

# 100: Este es el segundo argumento y representa el valor umbral. Todos los píxeles de la imagen que tengan un valor de intensidad mayor que 150 se establecerán en 255 (blanco) y todos los píxeles con un valor igual o menor a 150 se establecerán en 0 (negro).

# 255: Este es el tercer argumento y representa el valor máximo que se asignará a los píxeles que superen el valor umbral. En este caso, se establecerá en 255 (blanco).

# cv.THRESH_BINARY_INV: Este es el cuarto argumento y especifica el tipo de umbralización que se realizará. cv.THRESH_BINARY_INV es un tipo común de umbralización en el que los píxeles que superan el umbral se establecen en el valor máximo (255 en este caso) y los píxeles que no lo superan se establecen en el valor mínimo (0 en este caso). Pero de forma inversa, haciendo lo blanco negro y lo negro blanco

# cv.FILTER_BINARY: Este es el quinto argumento y especifica el tipo de filtro que se aplicará. En este caso, cv.FILTER_BINARY se utiliza para aplicar la umbralización binaria directamente.



cv.waitKey(0)
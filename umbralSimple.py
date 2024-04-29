import cv2 as cv

img=cv.imread("images/perro.jpg")
cv.imshow("imagen original", img )

#en el umbral (tresholding) se toma un pixel como referencia, y con respecto a este se compara si esta por debajo del pixel de referencia sera un pixel 0 negro y si esta por encima del pixel de referencia sera 1, la idea es binarisar la imagen, transformando sus pixeles en unos y ceros.
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# Umbral simple 
threshold, thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow("Umbral Simple",thresh)
# gray: Este es el primer argumento y representa la imagen en escala de grises en la que se aplicará la umbralización.

# 100: Este es el segundo argumento y representa el valor umbral. Todos los píxeles de la imagen que tengan un valor de intensidad mayor que 150 se establecerán en 255 (blanco) y todos los píxeles con un valor igual o menor a 150 se establecerán en 0 (negro).

# 255: Este es el tercer argumento y representa el valor máximo que se asignará a los píxeles que superen el valor umbral. En este caso, se establecerá en 255 (blanco).

# cv.THRESH_BINARY: Este es el cuarto argumento y especifica el tipo de umbralización que se realizará. cv.THRESH_BINARY es un tipo común de umbralización en el que los píxeles que superan el umbral se establecen en el valor máximo (255 en este caso) y los píxeles que no lo superan se establecen en el valor mínimo (0 en este caso).

# cv.FILTER_BINARY: Este es el quinto argumento y especifica el tipo de filtro que se aplicará. En este caso, cv.FILTER_BINARY se utiliza para aplicar la umbralización binaria directamente.



cv.waitKey(0)
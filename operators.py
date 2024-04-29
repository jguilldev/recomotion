import cv2 as cv
import numpy as np


#un pixel se enciende con un valor logico de 1 y se apaga con un valor logico de 0

blank=np.zeros((400,400),dtype="uint8")
#establece un lienzo de 400 x 400px

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
# blank.copy(): Esto crea una copia de la imagen en blanco para dibujar el rectángulo encima. Así no se modifica la original.

# (30,30): Son las coordenadas (x,y) de la esquina superior izquierda del rectángulo.

# (370,370): Las coordenadas de la esquina inferior derecha del rectángulo.

# 255: Es el valor de color o intensidad con el que se dibuja. 255 es color blanco.

# -1: Indica que se rellene el rectángulo con ese color. Si es otro valor como 1, solo dibuja el contorno.

circle=cv.circle (blank.copy(),(200,200),200,255,-1)

cv.imshow ("rectangulo", rectangle)
cv.imshow ("circulo", circle)


# el operador AND (interseccionado de imagenes)
AND=cv.bitwise_and(rectangle,circle)
cv.imshow ("AND", AND)
#mescla las dos imagenes obteniendo una tercera

# el operador OR (no intersecta e intersecta regiones)
OR=cv.bitwise_or(rectangle,circle)
cv.imshow ("OR", OR)
#devuelve los pixeles que se cruzan y los que no se cruzan obteniendo una tercera, basicamente sobrecruza las imagenes

# el operador XOR (no intersecta regiones)
XOR=cv.bitwise_xor(rectangle,circle)
cv.imshow ("XOR", XOR)
#devuelve los pixeles que se cruzan y los que no se cruzan obteniendo una tercera, basicamente sobrecruza las imagenes, cambiando o eliminando los pixeles que se cruzan al color del fondo.

# el operador NOT (INVIERTE EL COLOR BINARIO)
NOT=cv.bitwise_not(rectangle)
cv.imshow ("NOT", NOT)
#devuelve los pixeles INVERTIDOS CON RESPECTO AL FONDO




cv.waitKey(0)
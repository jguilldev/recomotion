import cv2 as cv
import numpy as np

#permite establecer un centro de atencion en una parte de la imagen
# por ejemplo en imagenes de personas podriamos centrarnos en el rostro, eliminando lo demas

img =cv.imread("images/perro.jpg")
cv.imshow("perro", img)

blank=np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank", blank)
# mg.shape[:2]: Toma las primeras 2 dimensiones de la forma (alto, ancho) de la imagen original. Así la imagen en blanco tendrá ese mismo alto y ancho.
# dtype="uint8": Indica el tipo de datos para los píxeles, en este caso uint8 que puede tomar valores entre 0 y 255. Es el tipo estándar para imágenes.
# np.zeros(): Crea una matriz numpy llena de ceros con las dimensiones y tipo de dato especificados.
# El primer parámetro (img.shape[:2]) define el tamaño (alto, ancho).
# El segundo (dtype) el tipo de valor para los píxeles.
# Al ser ceros, todos los píxeles tendrán intensidad 0 -> imagen en blanco.


# la mascara debe ser del mismo tamaño de la imagen de lo contrario, no va a funcionar
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("mascara", mask)

# blank: Es la imagen sobre la que se dibujará el círculo. Normalmente una imagen en blanco.
# (img.shape[1]//2, img.shape[0]//2): Son las coordenadas del centro del círculo. En este caso la mitad del ancho y alto de la imagen. (podemos sumar y restar aqui para ubicar la imagen)
# 100: Es el radio del círculo en píxeles.
# 255: Es el valor de color o intensidad del círculo. 255 es color blanco.
# -1: Indica que se rellene el círculo con ese color. Si no se pone, solo se dibuja el contorno.

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("seccion de enmascaramiento de la imagen",masked)


cv.waitKey(0)


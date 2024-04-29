import cv2 as cv
import numpy as np

img=cv.imread("images/perro.jpg")
cv.imshow("imagen original",img)

#los gradientes son regiones presentes en la imagen en forma de borde
# RECORDAR los gradientes son totalmente diferente de los bordes en una forma estrictamente matematica.

# Ademas del Kenny hay otras dos formas de encontrar aristas
# *laplaciana
# * el metodo soluble

# METODO LAPLACIANO
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("imagen en escala de grises",gray)

lap=cv.Laplacian(gray,cv.CV_64F)
# cv.Laplacian: aplica el operador Laplaciano a una imagen o matriz. Este operador se utiliza para detectar cambios bruscos en la intensidad de la imagen, lo que a menudo corresponde a bordes o características.

# gray: Es la imagen en escala de grises a la que se aplicará el operador Laplaciano. Este es el primer argumento de la función cv.Laplacian().

# cv.64F: Este es el segundo argumento y especifica el tipo de dato de salida para los resultados del operador Laplaciano. cv.64F se refiere a un tipo de dato de punto flotante de 64 bits, lo que significa que los resultados se almacenan como números con decimales en lugar de enteros. Esto es común en procesamiento de imágenes para preservar detalles sutiles en los bordes.
lap=np.uint8(np.absolute(lap))

# np.absolute(lap): Esta parte del código calcula el valor absoluto de cada elemento en la matriz lap. El valor absoluto asegura que todos los valores sean no negativos, ya que los cambios de intensidad pueden ser positivos o negativos en función de si la intensidad está aumentando o disminuyendo en un punto de la imagen.

# np.uint8(): Luego, el resultado del valor absoluto se convierte a un tipo de dato uint8 utilizando np.uint8(). Esto significa que los valores se representan como números enteros de 8 bits sin signo en el rango de 0 a 255. Esta conversión es común en procesamiento de imágenes para que los valores sean válidos para una imagen en escala de grises, donde 0 representa negro y 255 representa blanco.

# metodo soluble
sobelx= cv.Sobel(gray, cv.CV_64F,1,0)
sobely= cv.Sobel(gray, cv.CV_64F,0,1)
sobel_combinado= cv.Sobel(gray, cv.CV_64F,1,1)
soble_bitwise_or=cv.bitwise_or(sobelx,sobely)

# cv.Sobel(): Esta es una función de OpenCV que se utiliza para aplicar el operador Sobel a una imagen.

# gray: Es la imagen en escala de grises a la que se aplicará el operador Sobel. Es el primer argumento de la función.

# cv.CV_64F: Este es el segundo argumento y se utiliza para especificar el tipo de dato de salida para los resultados del operador Sobel. cv.CV_64F representa un tipo de dato de punto flotante de 64 bits, lo que significa que los resultados se almacenan como números con decimales para preservar detalles finos en los bordes.

# 1 y 0: Estos son los tercer y cuarto argumentos y se utilizan para especificar la dirección en la que se aplicará el operador Sobel. En este caso, 1 en el tercer argumento significa que se aplicará en la dirección horizontal (eje x) y 0 en el cuarto argumento indica que no se aplicará en la dirección vertical (eje y). Si uso 1,1 en el ultimo parametro se aplicara el sobel (soluble) a los dos ejes x y y

cv.imshow("soluble en x",sobelx)
cv.imshow("soluble en y",sobely)
cv.imshow("soluble en x y y",sobel_combinado)
cv.imshow("soluble en x y con or",soble_bitwise_or)

#comparacion con el detector de bordes Kenny
canny=cv.Canny(gray,150,175)
cv.imshow("canny", canny)

cv.imshow("laplaciano", lap)

cv.waitKey(0)
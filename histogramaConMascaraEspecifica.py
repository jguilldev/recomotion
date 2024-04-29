import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# el histograma permite ver una grafica de la intensidad de pixeles clasificando, cuales se repiten mas que otro dentro de la imagen o cuadro, es conveniente pasar la imagen a escala de grises, ya que la iluminacion, se toma mucho mejor, a menos que se este trabajando en un proyecto de distincion de colores

img=cv.imread("images/perro.jpg")
cv.imshow("perro", img) # muestra la imagen original

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("perro en escala de grises", gray) # muestra la imagen en escala de grises

#crear mascara
blank=np.zeros(img.shape[:2], dtype="uint8")

#np.zeros(img.shape[:2], dtype="uint8"): Esta expresión utiliza la biblioteca NumPy para crear una matriz de ceros con el mismo tamaño que la imagen original img. img.shape[:2] se refiere a las dos primeras dimensiones de la forma de la imagen, que representan la altura y el ancho de la imagen. dtype="uint8" especifica que los valores en la matriz de ceros serán enteros sin signo de 8 bits, lo que es adecuado para representar valores de intensidad en una imagen en escala de grises.

# En resumen, esta línea de código crea una imagen en blanco (blank) con el mismo tamaño que la imagen original img. La imagen en blanco se utiliza posteriormente para dibujar un círculo en ella.

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

# circle: Esta es la variable en la que se almacena el resultado de la función cv.circle(). Después de ejecutar esta línea, circle contendrá la imagen blank con un círculo blanco dibujado en ella.

# blank: Este es el primer argumento y representa la imagen en la que se va a dibujar el círculo. En este caso, se utiliza la imagen en blanco que creaste previamente con np.zeros().

# (img.shape[1]//2, img.shape[0]//2): Este es el segundo argumento y especifica el centro del círculo. (img.shape[1]//2, img.shape[0]//2) calcula el punto central utilizando las dimensiones de la imagen original img. img.shape[1] es el ancho de la imagen y img.shape[0] es la altura. Dividir estos valores por 2 da como resultado el centro de la imagen.

# 100: Este es el tercer argumento y representa el radio del círculo en píxeles. En este caso, se dibuja un círculo con un radio de 100 píxeles alrededor del centro especificado.

# 255: Este es el cuarto argumento y representa el valor de intensidad con el que se dibuja el círculo. En este caso, se utiliza el valor 255, que corresponde al color blanco en una imagen en escala de grises.

# -1: Este es el quinto argumento y especifica que el círculo se debe rellenar completamente. Si se establece en otro valor (por ejemplo, 1), solo se dibujaría el contorno del círculo, pero con -1, el círculo se rellena por completo.

mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow("mascara",mask)
# mask: Esto es una variable en la que se almacena el resultado de la operación bitwise_and. Después de ejecutar estas líneas, mask contendrá la imagen resultante después de aplicar la máscara circular al canal de intensidad en escala de grises.

# cv.bitwise_and(): Esta es la función de OpenCV utilizada para realizar la operación bitwise AND (AND a nivel de bits).

# gray: Este es el primer argumento y representa el canal de intensidad en escala de grises de la imagen original img. gray contiene los valores de intensidad de la imagen en escala de grises.

# gray: Este es el segundo argumento y es el mismo que el primero. Ambos argumentos representan el canal de intensidad en escala de grises de la imagen. En resumen, estás aplicando la operación bitwise_and entre el canal de intensidad y sí mismo, lo que esencialmente no cambia nada en este paso.

# mask=circle: Este es el tercer argumento y representa la máscara que se aplicará a la operación bitwise AND. En este caso, la máscara es un círculo blanco (como se creó previamente) que restringe la operación solo a la región del círculo.

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("perro en escala de grises", gray) # muestra la imagen en escala de grises

#histograma en escala de grises 
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
# Calculo el histograma en escala de grises con el methodo CALC_HIST

plt.figure() #establece una base para poner la figura
plt.title("histograma en escala de grises")#define titulo del grafico
plt.xlabel("contenedores")#pone nombre al eje x del grafico
plt.ylabel("# de pixeles")#pone nombre al eje y del grafico
plt.plot(gray_hist)#trae la imagen del histograma
plt.xlim([0,256])#define el rango a mostrarse en el eje x del grafico
plt.show()#muestra el grafico


cv.waitKey(0)
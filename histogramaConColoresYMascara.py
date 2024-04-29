import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# el histograma permite ver una grafica de la intensidad de pixeles clasificando, cuales se repiten mas que otro dentro de la imagen o cuadro, es conveniente pasar la imagen a escala de grises, ya que la iluminacion, se toma mucho mejor, a menos que se este trabajando en un proyecto de distincion de colores

img=cv.imread("images/perro.jpg")
cv.imshow("perro", img) # muestra la imagen original



#crear mascara
blank=np.zeros(img.shape[:2], dtype="uint8")

#np.zeros(img.shape[:2], dtype="uint8"): Esta expresión utiliza la biblioteca NumPy para crear una matriz de ceros con el mismo tamaño que la imagen original img. img.shape[:2] se refiere a las dos primeras dimensiones de la forma de la imagen, que representan la altura y el ancho de la imagen. dtype="uint8" especifica que los valores en la matriz de ceros serán enteros sin signo de 8 bits, lo que es adecuado para representar valores de intensidad en una imagen en escala de grises.

# En resumen, esta línea de código crea una imagen en blanco (blank) con el mismo tamaño que la imagen original img. La imagen en blanco se utiliza posteriormente para dibujar un círculo en ella.

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

# circle: Esta es la variable en la que se almacena el resultado de la función cv.circle(). Después de ejecutar esta línea, circle contendrá la imagen blank con un círculo blanco dibujado en ella.

# blank: Este es el primer argumento y representa la imagen en la que se va a dibujar el círculo. En este caso, se utiliza la imagen en blanco que creaste previamente con np.zeros().

# (img.shape[1]//2, img.shape[0]//2): Este es el segundo argumento y especifica el centro del círculo. (img.shape[1]//2, img.shape[0]//2) calcula el punto central utilizando las dimensiones de la imagen original img. img.shape[1] es el ancho de la imagen y img.shape[0] es la altura. Dividir estos valores por 2 da como resultado el centro de la imagen.

# 100: Este es el tercer argumento y representa el radio del círculo en píxeles. En este caso, se dibuja un círculo con un radio de 100 píxeles alrededor del centro especificado.

# 255: Este es el cuarto argumento y representa el valor de intensidad con el que se dibuja el círculo. En este caso, se utiliza el valor 255, que corresponde al color blanco en una imagen en escala de grises.

# -1: Este es el quinto argumento y especifica que el círculo se debe rellenar completamente. Si se establece en otro valor (por ejemplo, 1), solo se dibujaría el contorno del círculo, pero con -1, el círculo se rellena por completo.

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("mascara",masked)
# masked: Esto es una variable en la que se almacena el resultado de la operación bitwise_and. Después de ejecutar estas líneas, mask contendrá la imagen resultante después de aplicar la máscara circular al canal de intensidad en escala de grises.

# cv.bitwise_and(): Esta es la función de OpenCV utilizada para realizar la operación bitwise AND (AND a nivel de bits).

# gray: Este es el primer argumento y representa el canal de intensidad en escala de grises de la imagen original img. gray contiene los valores de intensidad de la imagen en escala de grises.

# gray: Este es el segundo argumento y es el mismo que el primero. Ambos argumentos representan el canal de intensidad en escala de grises de la imagen. En resumen, estás aplicando la operación bitwise_and entre el canal de intensidad y sí mismo, lo que esencialmente no cambia nada en este paso.

# mask=mask: Este es el tercer argumento y representa la máscara que se aplicará a la operación bitwise AND. En este caso, la máscara es un círculo blanco (como se creó previamente) que restringe la operación solo a la región del círculo.

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("perro en escala de grises", gray) # muestra la imagen en escala de grises

#histograma en escala de grises 
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
# Calculo el histograma en escala de grises con el methodo CALC_HIST

# plt.figure() #establece una base para poner la figura
# plt.title("histograma en escala de grises")#define titulo del grafico
# plt.xlabel("contenedores")#pone nombre al eje x del grafico
# plt.ylabel("# de pixeles")#pone nombre al eje y del grafico
# plt.plot(gray_hist)#trae la imagen del histograma
# plt.xlim([0,256])#define el rango a mostrarse en el eje x del grafico
# plt.show()#muestra el grafico

# histograma a color

plt.figure() #establece una base para poner la figura
plt.title("histograma en color")#define titulo del grafico
plt.xlabel("contenedores")#pone nombre al eje x del grafico
plt.ylabel("# de pixeles")#pone nombre al eje y del grafico

colors=("b","g","r") # se crea una tupla llamada colors que contiene tres elementos: "b", "g" y "r". Estas letras representan los canales de color azul (Blue), verde (Green) y rojo (Red) de una imagen en color RGB
for i, col in enumerate(colors):#Se inicia un bucle for que recorre cada elemento en la tupla colors. enumerate se utiliza para obtener tanto el valor (col, que representa "b", "g" o "r") como el índice (i, que representa 0, 1 o 2) de cada elemento en la tupla
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    
# [img]: Se pasa la imagen original img como una lista, indicando que estamos interesados en calcular el histograma de este canal de color específico.

# [i]: El valor de i representa el índice del canal de color actual (0 para azul, 1 para verde y 2 para rojo). Este argumento indica que estamos calculando el histograma para el canal de color correspondiente.

# mask: se usa la mascara

# [256]: Se especifica que queremos dividir el rango de valores de intensidad en 256 contenedores (bins) para el histograma.

# [0, 256]: Indica el rango de valores de intensidad que se incluirán en el histograma, desde 0 hasta 255.

    plt.plot(hist,color=col)
    plt.xlim([0,256])

#     plt.plot(hist, color=col): Luego de calcular el histograma para un canal de color específico, se utiliza plt.plot() de la biblioteca Matplotlib para trazar el histograma. El argumento hist es el histograma calculado y color=col especifica el color de la línea del gráfico, que corresponde al canal de color actual. dibuja en su color rojo,verde o blanco.

# plt.xlim([0,256]): Esto establece el rango que se muestra en el eje x del gráfico del histograma, asegurando que vaya desde 0 hasta 255 para representar todos los valores de intensidad posibles.

plt.show()
# plt.show(): Finalmente, después de calcular y trazar los histogramas para los tres canales de color (azul, verde y rojo), se utiliza plt.show() para mostrar los gráficos de histograma en una ventana gráfica.

cv.waitKey(0)
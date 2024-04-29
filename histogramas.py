import cv2 as cv
import matplotlib.pyplot as plt
# el histograma permite ver una grafica de la intensidad de pixeles clasificando, cuales se repiten mas que otro dentro de la imagen o cuadro, es conveniente pasar la imagen a escala de grises, ya que la iluminacion, se toma mucho mejor, a menos que se este trabajando en un proyecto de distincion de colores

img=cv.imread("images/perro.jpg")
cv.imshow("perro", img) # muestra la imagen original



gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("perro en escala de grises", gray) # muestra la imagen en escala de grises

#histograma en escala de grises 
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
# Calculo el histograma en escala de grises con el methodo CALC_HIST

# [gray] = es la imagen de la que se desea calcular

# [0] = indica los canales para una imagen gris el valor es 0
#  [0] para el canal azul (Blue).
#  [1] para el canal verde (Green).
#  [2] para el canal rojo (Red).
# aqui se usa 0 por que al convertirse a gris solo existe un canal de color (no es por que sea blue)

# # none  se refiere a la mascara como no tiene mascara se calcula para toda la imagen AQUI usamos none por que no estamos usando mascara

# [0, 256]:  especifica el rango de valores de intensidad que se incluirán en el histograma. En este caso, el rango va desde 0 hasta 255, que es el rango completo de valores de intensidad en una imagen en escala de grises.

# [256] se refiere al valor o numero de contenedores (llamados bin) en que se dividen el rango de valores de intensidad para este caso 255, es decir los niveles de intensidad de color por cada pixel en la imagen



plt.figure() #establece una base para poner la figura
plt.title("histograma en escala de grises")#define titulo del grafico
plt.xlabel("contenedores")#pone nombre al eje x del grafico
plt.ylabel("# de pixeles")#pone nombre al eje y del grafico
plt.plot(gray_hist)#trae la imagen del histograma
plt.xlim([0,256])#define el rango a mostrarse en el eje x del grafico
plt.show()#muestra el grafico

cv.waitKey(0)
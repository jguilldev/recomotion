import cv2 as cv
import numpy as np

img=cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

#Definir la función de traducción (linea 11): A continuación, se define una función llamada "translate" que realiza la traducción (traslación) de una imagen. La función toma tres argumentos: la imagen a traducir ("img"), y las cantidades de desplazamiento en el eje X e Y, respectivamente ("x" y "y"). La traducción se realiza utilizando una matriz de transformación afinada "transMat" que se crea con la función np.float32() de NumPy. Esta matriz de transformación se crea con los valores [1, 0, x] para el desplazamiento en el eje X y [0, 1, y] para el desplazamiento en el eje Y.


def translate(img,x,y):
    # La matriz 'transMat' se utiliza para realizar una traslación de la imagen.
    # El valor 'x' controla el desplazamiento en píxeles en el eje X,
    # mientras que el valor 'y' controla el desplazamiento en píxeles en el eje Y.
    # Los valores [1, 0, x] y [0, 1, y] en la matriz indican que no hay cambio de escala ni inclinación,
    # solo un desplazamiento en las direcciones especificadas.

    transMat=np.float32([[1,0,x],[0,1,y]])
    #El uso de np.float32 en NumPy es para convertir valores o listas de Python en números de punto flotante de 32 bits de precisión.
    dimensions=(img.shape[1],img.shape[0])
    # Obtiene las dimensiones de la imagen (ancho y altura) y las guarda en la tupla "dimensions". el tercer indice [] no usado se refiere a 
    return cv.warpAffine(img,transMat,dimensions)
    #Aplicar la traducción: La línea return cv.warpAffine(img, transMat, dimensions) aplica la traducción a la imagen utilizando la función cv.warpAffine(). Esta función toma como argumentos la imagen a transformar ("img"), la matriz de transformación afinada ("transMat"), y las dimensiones de la imagen de salida ("dimensions"). La función realiza la traslación de la imagen y devuelve la imagen trasladada.

translated=translate(img,100,100)#aqui se asigna el valor del desplazamiento en el eje x y y respectivamente, valores negativos en x y y hacen el desplazamiento hacia la izquierda y abajo reespectivamente
cv.imshow("translated",translated)
cv.waitKey(0)
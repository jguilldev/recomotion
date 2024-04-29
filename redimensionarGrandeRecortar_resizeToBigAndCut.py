import cv2 as cv
#ya vimos en este repositorio el redimencionamiento de imagenes en resizeimage.py, sin embargo se hace necesario usar interpolaciones cuando tomamos una imagen pequeña y queremos hacerla mas grande

img =cv.imread("images/smiley.jpg")

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
##INTER_LINEAR (Interpolación bilineal):Calcula el valor del nuevo píxel tomando un promedio ponderado de los cuatro píxeles más cercanos en la imagen original.ya que tiene en cuenta los píxeles vecinos y proporciona transiciones más suaves entre los píxeles.
#Es adecuado para la mayoría de las tareas de redimensionamiento y transformaciones geométricas.
#INTER_CUBIC (Interpolación cúbica):Utiliza una función polinómica de tercer orden para calcular el valor del nuevo píxel.
##Ofrece una calidad aún mejor que INTER_LINEAR, especialmente cuando se realiza un agrandamiento significativo, por lo que puede ser más lenta.
#Puede proporcionar resultados más suaves y detallados en imágenes con curvas o patrones complejos.

#las dos anteriores son utiles para hacer el redimencionamiento a imagenes mas grandes

cv.imshow('redimensionada con inter linear', resized)

#como las imagenes son matrices de pixeles, se puede recortar la matriz mediante cordenadas, como se ve a continuacion

cropped=img[50:200, 200:400]
cv.imshow('recorte de la matriz', cropped)

cv.waitKey(0)
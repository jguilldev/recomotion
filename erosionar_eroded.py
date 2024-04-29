import cv2 as cv
#enroded en si nos ayuda a adelgazar la linea y es util para eliminar ruido o delimitar objetos

img =cv.imread("images/smiley.jpg")

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#la linea anterior es la linea de la funcion de blur

canny=cv.Canny(img,125,175)
#la linea anterior hace difuminado de las lineas 
# 125: El valor umbral inferior. Píxeles con intensidades menores que este valor no se considerarán bordes.
# 175: El valor umbral superior. Píxeles con intensidades mayores que este valor se considerarán bordes.

dilated=cv.dilate(canny,(3,3),iterations=1)
#(3,3) es el tamaño del kernel (los pixeles a intervenir)
# iterations=1: Es el número de veces que se realizará la operación de dilatación. En este caso, se realiza una sola vez.

eroded=cv.erode(dilated,(3,3), iterations=1)

cv.imshow("Erosionado", eroded)


cv.waitKey(0)
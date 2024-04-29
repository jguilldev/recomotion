import cv2 as cv

img =cv.imread("images/smiley.jpg")

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#la linea anterior es la linea de la funcion de blur


#funcion para convertir la imagen a escala de gradientes dejando solamente la imagen y sus bordes
canny=cv.Canny(img,125,175)
#si en esta linea remplazamos img por blur agregando el respectivo codigo que se encuentra en blur.py en este mismo repositorio se lograra eliminar las lineas inecesarias, ya que se combina el difuminado, con las lineas es decir : canny=cv.Canny(blur,125,175)
cv.imshow("Bordes de imagen",canny)

cv.waitKey(0)
import cv2 as cv

img =cv.imread("images/smiley.jpg")
# cv.imshow("smile", img)
#la linea anterior solo dibuja la imagen original por eso esta comentada
cv.waitKey(0)

#funcion para convertir la imagen a escala de grises
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)

cv.waitKey(0)
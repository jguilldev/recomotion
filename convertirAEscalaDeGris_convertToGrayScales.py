import cv2 as cv

img =cv.imread("images/smiley.jpg")
#BGR es la forma predeterminada de mostrar la imagen
cv.imshow("smile", img)

#de BGR a escala de gris
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("de BGR a escala de grises", gray)

cv.waitKey(0)
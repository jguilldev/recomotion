# Este es un ejemplo de cómo leer una imagen con la biblioteca OpenCV.
import cv2 as cv

img =cv.imread("images/smiley.jpg")
cv.imshow("smile", img)
cv.waitKey(0)
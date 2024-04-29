import cv2 as cv

img =cv.imread("images/smiley.jpg")
#BGR es la forma predeterminada de mostrar la imagen
cv.imshow("smile", img)

#de BGR a HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("de BGR a HSV", hsv)

cv.waitKey(0)
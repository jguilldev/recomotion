import cv2 as cv

img =cv.imread("images/smiley.jpg")
#BGR es la forma predeterminada de mostrar la imagen
cv.imshow("smile", img)

#de BGR a LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("de BGR a LAB", lab)

cv.waitKey(0)
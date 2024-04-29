import cv2 as cv
import numpy as np

img = cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) 
#usando cubic la respuesta es mas lenta pero la imagen resultante es mejor
cv.imshow("redimensionado iterpolation-cubic", resize)
cv.waitKey(0)
cv.destroyAllWindows()
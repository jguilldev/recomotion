import cv2 as cv
import numpy as np

img = cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

# Realizar volteos en diferentes direcciones
flip_vertical = cv.flip(img, 0)  # Volteo vertical (eje y)
flip_horizontal = cv.flip(img, 1)  # Volteo horizontal (eje x)
flip_both = cv.flip(img, -1)  # Volteo en ambos ejes (horizontal y vertical)

cv.imshow("volteo vertical", flip_vertical)
cv.imshow("volteo horizontal", flip_horizontal)
cv.imshow("volteo en ambos ejes", flip_both)
cv.waitKey(0)
cv.destroyAllWindows()
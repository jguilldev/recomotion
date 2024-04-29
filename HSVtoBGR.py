import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images/smiley.jpg")

# Convierte la imagen de BGR a HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Muestra la imagen en OpenCV después de la conversión a HSV
cv.imshow("BGR --> HSV", hsv)

# Espera hasta que se presione una tecla
cv.waitKey(0)

# Convierte la imagen de HSV a BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# Muestra la imagen en OpenCV después de la conversión a BGR
cv.imshow("HSV --> BGR", hsv_bgr)

# Espera hasta que se presione una tecla
cv.waitKey(0)

# Cierra la ventana de imagen
cv.destroyAllWindows()

# Convierte la imagen de BGR a RGB para mostrarla en Matplotlib
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Muestra la imagen en Matplotlib
plt.imshow(rgb)

# Muestra la ventana de Matplotlib
plt.show()
# Espera hasta que se presione una tecla
cv.waitKey(0)

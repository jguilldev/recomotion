import cv2 as cv
import matplotlib.pyplot as plt

# Lee la imagen de entrada
img = cv.imread("images/smiley.jpg")

# Convierte la imagen de LAB a BGR
lab_bgr = cv.cvtColor(img, cv.COLOR_LAB2BGR)

# Muestra la imagen en OpenCV después de la conversión a BGR
cv.imshow("LAB --> BGR", lab_bgr)

# Espera hasta que se presione una tecla
cv.waitKey(0)

# Cierra la ventana de imagen de OpenCV
cv.destroyAllWindows()

# Convierte la imagen de BGR a RGB para mostrarla en Matplotlib
rgb = cv.cvtColor(lab_bgr, cv.COLOR_BGR2RGB)

# Muestra la imagen en Matplotlib
plt.imshow(rgb)

# Muestra la ventana de Matplotlib
plt.show()

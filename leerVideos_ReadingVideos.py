import cv2 as cv

captura = cv.VideoCapture("videos/robot.mp4")  # 0, 1, 2 o 3 para cámaras
while True:  # hacer un bucle infinito mientras se cumple alguna condición
    esCorrecto, fotograma = captura.read()
    cv.imshow("video", fotograma)  # capturar el fotograma

    if cv.waitKey(20) & 0xFF == ord("d"):  # esperar 20ms para presionar la tecla
        break

captura.release()
cv.destroyAllWindows()

cv.waitKey(0)

# En la línea cuatro, sus parámetros pueden ser números 0, 1, 2, etc., donde 0 es la cámara predeterminada de tu PC, 1 es la segunda cámara y 2 es la tercera cámara.
#
# O puedes usar una ruta relativa, por ejemplo, c/video/robot.mp4

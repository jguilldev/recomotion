#este metodo de capture.set funciona para capturar frames en vivo, y funciona para imagenes y video.

import cv2 as cv

# Abre la cámara
capture = cv.VideoCapture(1)  # 0 para la cámara predeterminada, puedes cambiarlo según el índice de tu cámara

# Verifica si se abrió la cámara correctamente
if not capture.isOpened():
    print("No se pudo abrir la cámara")
    exit()

# Define el nuevo ancho y altura deseados
new_width = 320
new_height = 240

# Cambia el ancho y altura de la cámara utilizando el método capture.set()
capture.set(cv.CAP_PROP_FRAME_WIDTH, new_width)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, new_height)

# Lee y muestra los fotogramas de la cámara en tiempo real
while True:
    ret, frame = capture.read()
    if not ret:
        break

    cv.imshow("Video", frame)

    # Si se presiona la tecla 'e', se termina el proceso
    if cv.waitKey(1) == ord('e'):
        break

# Libera los recursos
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)

import dlib
import cv2

# Inicializar el detector de rostros de dlib
detector = dlib.get_frontal_face_detector()

# Inicializar la captura de video desde la cámara (en este caso, la cámara 0)
captura = cv2.VideoCapture(0)

while True:
    # Leer un frame de la cámara
    ret, frame = captura.read()

    # Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el frame usando dlib
    rostros = detector(gris)

    # Dibujar rectángulos alrededor de los rostros detectados
    for rostro in rostros:
        x, y, w, h = rostro.left(), rostro.top(), rostro.width(), rostro.height()
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Mostrar el frame con los rostros detectados
    cv2.imshow('Detección de Rostros en Tiempo Real', frame)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
captura.release()
cv2.destroyAllWindows()

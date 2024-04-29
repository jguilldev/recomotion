import cv2 as cv

# Cargar el clasificador en cascada Haar para la detección facial
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Iniciar la captura de video desde la cámara (puedes cambiar el argumento a un archivo de video si prefieres)
cap = cv.VideoCapture("images/video.mp4")  # Usar 0 para la cámara predeterminada

while True:
    # Leer un fotograma del flujo de video
    ret, frame = cap.read()

    # Convertir el fotograma a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectar rostros en el fotograma utilizando el clasificador Haar
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    # Mostrar el fotograma con los rectángulos alrededor de los rostros detectados
    cv.imshow("Detección de Rostros", frame)

    # Presiona 'q' para salir del bucle
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar todas las ventanas
# Espera hasta que se presione una tecla
cv.waitKey(0) 

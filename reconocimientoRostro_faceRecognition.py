# Para usar este archivo, antes se debe haber realizado, el modelo de entrenamiento, con las imagenes
# pertinentes, como se muestra en el archivo "generadorPequenoModeloEntrenamiento_generatorModelTrainigForRecognized.py"
# presente en este mismo repositorio de gitHub, junto con las imagenes de los artistas a su eleccion,
# puedes descargar facilmente imagenes para entrenamiento con mi proyecto de github "https://github.com/jguilldev/DescargaImagenes"

import cv2
import numpy as np

# Carga el modelo entrenado
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Lista de artistas (debe coincidir con el orden usado durante el entrenamiento)
people = ['Amy Winehouse', 'David Bowie', 'Freddie Mercury', 'Kurt Cobain', 'Ozzy Osbourne']

# Ruta del archivo Haar Cascade
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ruta al video que deseas procesar
video_path = './videos/amy.mp4'  #  Se debe cambia a la ruta en donde esta el video

# Carga el video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error al abrir el video") #manejo de errores
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Fin del video o error al leer el marco")
        break

    # Convierte cada frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta los rostros en el frame
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]  # Selecciona la región de interés (el rostro)

        # Realiza la predicción
        label, confidence = face_recognizer.predict(faces_roi)

        # Dibuja el rectángulo alrededor del rostro
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Muestra el nombre del artista y el nivel de confianza
        cv2.putText(frame, f'{people[label]} ({int(confidence)})', (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Muestra el frame con las detecciones
    cv2.imshow('Video - Reconocimiento Facial', frame)

    # Presiona 'q' para salir del video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()
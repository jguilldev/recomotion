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

# Ruta de la imagen que deseas procesar
image_path = 'images/simple_images/Amy Winehouse/Amy Winehouse_3.jpg'  # Cambia a la ruta donde está tu imagen

# Carga la imagen
image = cv2.imread(image_path)
if image is None:
    print("Error al cargar la imagen")  # Manejo de errores
    exit()

# Redimensiona la imagen a un tamaño más manejable
output_width = 640
output_height = 480
image = cv2.resize(image, (output_width, output_height))

# Convierte la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecta los rostros en la imagen
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]  # Selecciona la región de interés (el rostro)

    # Realiza la predicción
    label, confidence = face_recognizer.predict(faces_roi)

    # Dibuja el rectángulo alrededor del rostro
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Muestra el nombre del artista y el nivel de confianza
    cv2.putText(image, f'{people[label]} ({int(confidence)})', (x, y-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# Muestra la imagen procesada
cv2.imshow('Imagen - Reconocimiento Facial', image)

# Presiona cualquier tecla para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

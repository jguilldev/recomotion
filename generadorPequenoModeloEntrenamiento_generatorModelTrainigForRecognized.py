# Este codigo genera un archivo ".yml", que es un generador de "modelo entrenado" de acuerdo a las fotos de  las carpetas, para usar en el reconocedor real
# se debe modificar la ruta en la linea 13, ael sitio donde estan las fotos y carpetas de las personas a entrenar
import os
import cv2
import numpy as np

# Lista de personas basada en las carpetas visiblesanteriormente creadas dentro del proyecto
#una para cada artista
people = ['Amy Winehouse', 'David Bowie', 'Freddie Mercury', 'Kurt Cobain', 'Ozzy Osbourne']

# cargamos DIR con la ruta donde estan alojadas nuestras carpetas
# con los nombres y fotos de cada artista
DIR = './images/simple_images' 

# Ruta al clasificador Haar Cascade dentro de nuestro proyecto hay un archivo de entrenamiento llamado
# haar_face_xml, descargado anteriormente de https://github.com/opencv/opencv/tree/master/data/haarcascades.
haar_cascade = cv2.CascadeClassifier('./haar_face.xml')

# Listas para almacenar características (features) y etiquetas (labels), son las etiquetas de la imagenes entrenadas
# deben tener un array donde guardarse
features = []
labels = []

# Función para entrenar el modelo
def create_train():
    for person in people:
        path = os.path.join(DIR, person)  # Ruta completa a la carpeta de cada persona
        label = people.index(person)  # Etiqueta numérica basada en el índice

        if not os.path.exists(path):  # Verifica si la carpeta existe
            print(f"Carpeta no encontrada: {path}")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)  # Ruta completa de cada imagen

            img_array = cv2.imread(img_path)
            if img_array is None:
                print(f"Error al cargar la imagen: {img_path}")
                continue

            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Entrenamiento completado ---------------')

# Convierte las listas a arrays de NumPy
features = np.array(features, dtype='object')
labels = np.array(labels)

# Crea el reconocedor de rostros (Que se debe ajustar según la versión de OpenCV en este caso cv2)
try:
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
except AttributeError:
    face_recognizer = cv2.face.LBPH_create()

# Entrena el modelo con los datos de arrays features y labels
face_recognizer.train(features, labels)

# Guarda el modelo entrenado creando un archivo .yml llamado face_trained (entrenamiento de caras)
face_recognizer.save('face_trained.yml')

# Guarda los datos de características y etiquetas
np.save('features.npy', features)
np.save('labels.npy', labels)

# el archivo  face_trained (entrenamiento de caras) ya queda listo para que nosotros,
# lo podamos utilizar en algun otro sitio que necesitemos
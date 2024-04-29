import os
import cv2
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'C:\Users\joseg\Desktop\MARCA PERSONAL\ProyectRecEmotion\images\caras' 

haar_cascade = cv2.CascadeClassifier(r'C:\Users\joseg\Desktop\MARCA PERSONAL\ProyectRecEmotion\haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person) 
        label = people.index(person)  

        for img in os.listdir(path):
            img_path = os.path.join(path, img)  

            img_array = cv2.imread(img_path)

            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)         

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# Utiliza la nueva forma de crear el reconocedor
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# O también puedes probar con el siguiente método
# face_recognizer = cv2.face.LBPH_create()

# face_recognizer.train(features, labels)

# Guarda el modelo entrenado
face_recognizer.save('face_trained.yml')

# Guarda los datos de características y etiquetas
np.save('features.npy', features)
np.save('labels.npy', labels)

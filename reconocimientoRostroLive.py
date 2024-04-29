import cv2
import numpy as np

#es necesario una maquina con buena resolucion para que el programa funcione
#Yo use droidcam ya que mi camara tiene baja calidad, y este programa permite enlazar mi  telefono
# movil al programa en el computador

# Cargar el modelo entrenado
modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
configFile = "deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

# Iniciar la captura de video desde la cámara web integrada (0)
cap = cv2.VideoCapture(1)  # Usar 0 para la cámara predeterminada

while True:
    # Leer un fotograma del flujo de video
    ret, frame = cap.read()

    # Obtener el tamaño del fotograma
    h, w = frame.shape[:2]

    # Preprocesar la imagen para la detección de caras
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), [104, 117, 123], False, False)

    # Detectar caras en el fotograma
    net.setInput(blob)
    detections = net.forward()

    # Iterar detecciones y dibujar bounding box
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)

    # Mostrar el fotograma resultante con las caras detectadas
    cv2.imshow("Reconocimiento de Rostros en Vivo", frame)

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()



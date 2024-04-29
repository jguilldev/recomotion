# La primera parte del código define una función para cambiar el tamaño
import cv2 as cv

def redimensionarFotograma(fotograma, escala=0.75):
    ancho = int(fotograma.shape[1] * escala)
    alto = int(fotograma.shape[0] * escala)
    dimensiones = (ancho, alto)
    return cv.resize(fotograma, dimensiones, interpolation=cv.INTER_AREA)

# La segunda parte del código captura y muestra los fotogramas

captura = cv.VideoCapture("videos/robot.mp4")
while True:
    esCorrecto, fotograma = captura.read()
    fotograma_redimensionado = redimensionarFotograma(fotograma, escala=0.2)
    # es posible cambiar el tamaño agregando un parámetro a la línea anterior
    # fotograma_redimensionado = redimensionarFotograma(fotograma, escala=0.2) y cambiar el número por una escala menor
    cv.imshow("video", fotograma)
    cv.imshow("video Redimensionado", fotograma_redimensionado)

    if cv.waitKey(150) & 0xFF == ord("d"):  # es posible cambiar el tiempo para cerrar la ventana, para que el sistema operativo crea que la ventana no responde
        break

    # Verifica si el usuario hizo clic en el botón de cierre en alguna de las ventanas
    if cv.getWindowProperty("video", cv.WND_PROP_VISIBLE) < 1 or cv.getWindowProperty("video Redimensionado", cv.WND_PROP_VISIBLE) < 1:
        break

captura.release()
cv.destroyAllWindows()

cv.waitKey(0)

# Nota: Redimensionar los fotogramas puede afectar la velocidad del video,
# ya que requiere tiempo de procesamiento adicional. Cuanto más grande sea el video y
# más intensa sea la redimensión, mayor será el impacto en la velocidad. El
# rendimiento también puede verse influenciado por las capacidades del procesador de la computadora,
# ya que un procesador más rápido con más núcleos puede manejar la redimensión
# de manera más eficiente, lo que resulta en una reproducción de video más rápida y fluida.

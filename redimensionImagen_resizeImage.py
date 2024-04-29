# Importamos la biblioteca OpenCV y la renombramos como "cv"
import cv2 as cv

# Definimos una función llamada "rescaleImage" que recibe una imagen y una escala (opcional)
def rescaleImage(imagen, escala=0.75):
    # Calculamos el nuevo ancho y alto de la imagen multiplicando sus dimensiones originales por la escala
    ancho = int(imagen.shape[1] * escala)
    alto = int(imagen.shape[0] * escala)
    
    # Creamos una tupla con las nuevas dimensiones
    dimensiones = (ancho, alto)
    
    # Utilizamos la función "cv.resize" para redimensionar la imagen a las nuevas dimensiones
    # Usamos "interpolation=cv.INTER_AREA" para determinar cómo se realiza la interpolación al cambiar el tamaño
    imagen_redimensionada = cv.resize(imagen, dimensiones, interpolation=cv.INTER_AREA)
    
    # Retornamos la imagen redimensionada
    return imagen_redimensionada

# Cargamos una imagen desde el archivo "smiley.jpg" en una variable llamada "imagen"
imagen = cv.imread("images/smiley.jpg")

# Llamamos a la función "rescaleImage" para redimensionar la imagen cargada previamente
# Con "escala=0.5" estamos indicando que queremos reducir la imagen a la mitad de su tamaño original
imagen_redimensionada = rescaleImage(imagen, escala=0.5)

# Mostramos la imagen original en una ventana con el título "Imagen"
cv.imshow("Imagen Original", imagen)

# Mostramos la imagen redimensionada en otra ventana con el título "Imagen Redimensionada"
cv.imshow("Imagen Redimensionada", imagen_redimensionada)

# Esperamos hasta que el usuario presione una tecla (0 indica espera infinita)
cv.waitKey(0)

# Cerramos todas las ventanas abiertas
cv.destroyAllWindows()

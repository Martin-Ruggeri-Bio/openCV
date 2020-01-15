import numpy as np
import cv2

# Cargar imagen
imagen = cv2.imread("imagen/robot-vision-artificial.jpg")

# Mostramos imagen
cv2.imshow("original",imagen)

# Obtenemos el ancho y el alto
ancho = imagen.shape[1]
alto = imagen.shape[0]
print("ancho: {} pixeles".format(ancho))
print("alto: {} pixeles".format(alto))

# Calcular punto de rotación, centro imagen


# Obtenemos la matriz de transformación, rotación
M = cv2.getRotationMatrix2D(puntoRotacion, 85, 1.0)

# Rotamos imagen
imagenRotada = cv2.warpAffine(imagen, M, (ancho, alto))

# Mostrar la imagen rotada
cv2.imshow("imagenrotada1", imagenRotada)
cv2.waitKey(0)
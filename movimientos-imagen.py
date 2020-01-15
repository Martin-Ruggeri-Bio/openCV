import cv2
import numpy as np 
import funciones
#leer una imagen
imagen=cv2.imread("imagen/robot-vision-artificial.jpg")
# Mostramos original
funciones.mostrarimg("original",imagen)

traslacion=funciones.traslacion(imagen,-100,-100)

funciones.mostrarimg("traslada-abajo",traslacion)

# Obtenemos la matriz de transformación, rotación

imagenrotada=funciones.rotacion(imagen,85)
# Mostrar la imagen rotada

funciones.mostrarimg("imagenrotada",imagenrotada)

anchopunto=int(input("ingresa una cordenada dentro de los pixeles"))
altopunto=int(input("ingresa una cordenada dentro de los pixeles"))
imagenrotadapunto=funciones.rotacionpunto(imagen,anchopunto,altopunto,50)
funciones.mostrarimg("imagenrotadapunto",imagenrotadapunto)
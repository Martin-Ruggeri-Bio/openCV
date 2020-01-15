import cv2
import numpy as np
from funciones import mostrarimg
# Creamos una imagen negra de 300x300
# un canvas es un lugar donde dibujar
canvas = np.zeros((300,300,3),dtype="uint8")
 
# Color verde puro
verde = (0,255,0)
# Dibujamos línea
cv2.line(canvas,(0,0),(150,150),verde)
 
# Mostrar imagen
mostrarimg("canvas",canvas)
 
# Dibujamos línea con grosor 4
cv2.line(canvas,(150,0),(150,150),verde,4)
#Dibujar círculo relleno
cv2.circle(canvas,(150,150),75,verde,-1)
# Mostrar imagen
mostrarimg("canvas",canvas)
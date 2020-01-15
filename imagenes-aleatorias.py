import cv2
import numpy as np
from funciones import mostrarimg
# Creamos imagen negra
canvas = np.zeros((500,500,3),dtype=("uint8"))
 
# Dibujamos 25 círculos
for i in range(0,25,1):
 
 # Radio aleatorio entre 5 y 200
 radio = np.random.randint(5,high=200)
 
 # Color aleatorio en bgr
 color= np.random.randint(0,high=255,size=(3,)).tolist()
 
 # Centro aleatorio
 centro = np.random.randint(0,high=500,size=(2,))
 
 # Dibujar el cículo aleatorio
 cv2.circle(canvas,tuple(centro),radio,color,-1)
# Mostramos la imagen
 mostrarimg("canvas",canvas)


import cv2
import numpy as np

def mostrarimg(nombre,imagen):
	# Mostrar imagen
	cv2.imshow(nombre, imagen)
	cv2.waitKey(0)
	return

def traslacion(imagen, x, y):
	
	# Matriz de transformación
	M = np.float32([[1,0,x],[0,1,y]])
	# Aplicamos traslación a la imagen
	imtraslacion =  cv2.warpAffine(imagen,M,(imagen.shape[1],imagen.shape[0]))
	# Devolvemos la imagen trasladada
	return imtraslacion 

def rotacion(imagen,angulo):
	# Obtenemos el ancho y el alto
	ancho = imagen.shape[1]
	alto = imagen.shape[0]
	print("ancho: {} pixeles".format(ancho))
	print("alto: {} pixeles".format(alto))
	puntorot = (ancho//2, alto//2)
	M = cv2.getRotationMatrix2D(puntorot,angulo, 1.0)
	# Rotamos imagen
	imagenrotada = cv2.warpAffine(imagen, M, (ancho,alto))
	return imagenrotada
def rotacionpunto(imagen,anchopunto,altopunto,angulo):
	# Obtenemos el ancho y el alto
	ancho = imagen.shape[1]
	alto = imagen.shape[0]
	puntorot=(anchopunto,altopunto)
	M = cv2.getRotationMatrix2D(puntorot,angulo, 1.0)
	# Rotamos imagen
	imagenrotadapunto = cv2.warpAffine(imagen, M, (ancho,alto))
	
	
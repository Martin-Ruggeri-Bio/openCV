import cv2
imagen = cv2.imread("imagen/robot-vision-artificial.jpg")

print("ancho: {} pixels".format(imagen.shape[1]))
print("alto: {} pixels".format(imagen.shape[0]))
print("canales: {} pixels".format(imagen.shape[2]))

# Mostramos la imagen en la pantalla
cv2.imshow("visor", imagen)
cv2.waitKey(0)
# Guardar la imagen con otro nombre y otro formato
# Solo hay que poner la extensión del formato que queramos guardar
cv2.imwrite("imagen/nueva-imagen.png",imagen)
# Obtener el pixel (0,0)
(b, g, r) = imagen[0,0]
print("Pixel (0,0) => Roja {}, Verde {}, Azul {}".format(r,g,b))
# Cambiamos el color del pixel (0,0)
'''for i in range(10):
	for j in range(10):
		imagen[i,j] = (0,0,255)
		(b, g, r) = imagen[i,j]
	#	print("Pixel (", str(i) , "," , str(j) , ") => Roja {}, Verde {}, Azul {}".format(r,g,b))
		print("Pixel ({},{}) => Roja {}, Verde {}, Azul {}".format(i,j,r,g,b))
cv2.imshow("visor", imagen)
cv2.waitKey(0)'''
# Obtener region cuadrada
region = imagen[0:150,0:150]
cv2.imshow("region", region)
cv2.waitKey(0)
 
# Obtener rectangular ancho
region = imagen[0:100, 0:150]
cv2.imshow("region2", region)
cv2.waitKey(0)
 
# Obtener rectangular alto
region = imagen[0:150, 0:100]
cv2.imshow("region3", region)
cv2.waitKey(0)
#cambiar region de la imagen
imagen[100:200,100:200]=(200,100,200)
cv2.imshow("imagen cambiada", imagen)
cv2.waitKey(0)

import cv2
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

imagen = cv2.imread("imagen/robot-vision-artificial.jpg")

print("ancho: {} pixels".format(imagen.shape[1]))
print("alto: {} pixels".format(imagen.shape[0]))
print("canales: {} pixels".format(imagen.shape[2]))
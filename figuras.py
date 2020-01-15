import cv2
imagen = cv2.imread("imagen/robot-vision-artificial.jpg")
color=(200,100,200)
grosor=5
(p1x,p1y)=(50,50)
(p2x,p2y)=(200,200)
radio=p2x-p1x
cv2.line(imagen,(p1x,p1y),(p2x,p2y),color,grosor)
cv2.rectangle(imagen,(p1x,p1y),(p2x,p2y),color,grosor)
cv2.circle(imagen,(p1x,p2x),radio,color,grosor)
cv2.imshow("visor", imagen)
cv2.waitKey(0)
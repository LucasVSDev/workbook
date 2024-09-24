import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector

webcam = cv2.VideoCapture(0)
rastreador = FaceDetector(minDetectionCon= 0.5, modelSelection= 1)
rastreador2 = HandDetector(detectionCon= 0.9, maxHands= 4)

while True:
    sucesso, image = webcam.read()
    coordenadas, imagem_rosto = rastreador.findFaces(image, draw=False)
    coordenadas2, imagem_maos = rastreador2.findHands(image)
    
    print(coordenadas)
    
    cv2.imshow("Projeto 4 - IA", image)
    
    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()
    
    
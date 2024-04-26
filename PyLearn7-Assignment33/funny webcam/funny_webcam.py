import cv2
import numpy as np

image = cv2.imread("input/mozart.jpg", cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture(0)
box = np.zeros((110, 110), dtype=int)

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    image[385:520,555:705] = frame [60:195,290:440]
    
    cv2.imshow("funny webcam", image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break



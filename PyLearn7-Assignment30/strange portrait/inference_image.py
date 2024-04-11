import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel



fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

image = cv2.imread("input\image4.jpg")
image = cv2.rotate(image, 1)
color = (125, 255, 125)

start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    # for i, p in enumerate(np.round(pred).astype(np.int32)):
        # cv2.circle(image, tuple(p), 2, color, -1, cv2.LINE_AA)
        # cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 0))

    lips_landmarks = []
    for i in [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]:
        lips_landmarks.append(pred[i])
    lips_landmarks = np.array(lips_landmarks, dtype=int)

    left_eye_landmarks = []
    for i in [35, 36, 33, 37, 39, 42, 40, 41, 35]:
        left_eye_landmarks.append(pred[i])
    left_eye_landmarks = np.array(left_eye_landmarks, dtype=int)

    right_eye_landmarks = []
    for i in [89, 90, 87, 91, 93, 96, 94, 95]:
        right_eye_landmarks.append(pred[i])
    right_eye_landmarks = np.array(right_eye_landmarks, dtype=int)


    x, y, w, h = cv2.boundingRect(lips_landmarks)
    mask = np.zeros(image.shape, dtype=np.uint8)
    cv2.drawContours(mask, [lips_landmarks], -1, (255, 255, 255), -1)
    mask = mask // 255
    
    lips = image * mask
    lips = lips [y:y+h, x:x+w]
    hh, ww, _ = lips.shape
    

    for i in range(hh):
        for j in range(ww):
            if lips[i][j][0] == 0 and lips[i][j][1] == 0 and lips[i][j][2] == 0:
                lips[i][j] = image[y+i, x+j]

    lips_rotated = cv2.rotate(lips, 1)
    image[y:y + hh, x:x + ww] = lips_rotated

    

print(time.perf_counter() - start_time)

cv2.imshow("result", lips)
cv2.waitKey()
cv2.imwrite("output/tt2.jpg", image)


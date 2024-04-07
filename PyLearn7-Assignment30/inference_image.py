import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

image = cv2.imread("input\image11.jpg")
color = (125, 255, 125)

start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    for p in np.round(pred).astype(np.int32):
        cv2.circle(image, tuple(p), 2, color, -1, cv2.LINE_AA)

print(time.perf_counter() - start_time)

cv2.imshow("result", image)
cv2.waitKey()


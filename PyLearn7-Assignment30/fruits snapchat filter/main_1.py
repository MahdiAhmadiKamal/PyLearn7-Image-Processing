import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def fruit_filter (file_path, landmark):

    fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

    image = cv2.imread(file_path)
    fruit = cv2.imread("input/apple.jpg")

    color = (125, 255, 125)

    start_time = time.perf_counter()

    boxes, scores = fd.inference(image)

    for pred in fa.get_landmarks(image, boxes):
        
        # for i, p in enumerate(np.round(pred).astype(np.int32)):
        #     cv2.circle(image, tuple(p), 2, color, -1, cv2.LINE_AA)
        #     cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 0))
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

        # face_organs = [lips_landmarks, left_eye_landmarks, right_eye_landmarks]

        # for face_organ in face_organs:
        if landmark == "lips":
            organ_landmarks = lips_landmarks
        if landmark == "left eye":
            organ_landmarks = left_eye_landmarks
        if landmark == "right eye":
            organ_landmarks = right_eye_landmarks

        x, y, w, h = cv2.boundingRect(organ_landmarks)
        mask = np.zeros(image.shape, dtype=np.uint8)
        cv2.drawContours(mask, [organ_landmarks], -1, (255, 255, 255), -1)
        mask = mask // 255

        result = image * mask
        result = result [y:y+h, x:x+w]

        result_big = cv2.resize(result, (0, 0), fx=6, fy=6)
        hh, ww, _ = result_big.shape
    
        hhh, www, _ = fruit.shape
        lips_loc = [int(hhh//1.7), int(www//2.65)]
        left_eye_loc = [int(hhh//2.3), int(www//2.8)]
        right_eye_loc = [int(hhh//2.3), int(www//1.9)]
    
        if landmark == "lips":
            for i in range(hh):
                for j in range(ww):
                    if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                        result_big[i][j] = fruit[lips_loc[0]+i, lips_loc[1]+j]
            fruit[lips_loc[0]:lips_loc[0] + hh, lips_loc[1]:lips_loc[1] + ww] = result_big
                            
        if landmark == "left eye":
            for i in range(hh):
                for j in range(ww):
                    if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                        result_big[i][j] = fruit[left_eye_loc[0]+i, left_eye_loc[1]+j]
            fruit[left_eye_loc[0]:left_eye_loc[0] + hh, left_eye_loc[1]:left_eye_loc[1] + ww] = result_big

        if landmark == "right eye":
            for i in range(hh):
                for j in range(ww):
                    if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                        result_big[i][j] = fruit[right_eye_loc[0]+i, right_eye_loc[1]+j]
            fruit[right_eye_loc[0]:right_eye_loc[0] + hh, right_eye_loc[1]:right_eye_loc[1] + ww] = result_big
        
    
    print(time.perf_counter() - start_time)

    # cv2.imshow("result", result_big)
    cv2.waitKey()
    cv2.imwrite("output/" + landmark + ".jpg", result_big)
    cv2.imwrite("input/apple.jpg", fruit)
    
    return result_big
    

fruit_filter("input\image22.jpg", "lips")
fruit_filter("input\image22.jpg", "left eye")
fruit_filter("input\image22.jpg", "right eye")
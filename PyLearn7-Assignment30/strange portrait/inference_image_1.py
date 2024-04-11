import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

# apple = cv2.imread("input/apple2.jpg")
def effect (file_path, landmark):

    fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

    image = cv2.imread(file_path)
    apple = cv2.imread("input/apple2.jpg")
    # apple = apple.astype(np.float32)
    # print(apple)
    color = (125, 255, 125)

    start_time = time.perf_counter()

    boxes, scores = fd.inference(image)

    for pred in fa.get_landmarks(image, boxes):
        
        # for i, p in enumerate(np.round(pred).astype(np.int32)):
        #     cv2.circle(image, tuple(p), 2, color, -1, cv2.LINE_AA)
        #     cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 0))
        organ_landmarks = []
        if landmark == "lips":
            for i in [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]:
                organ_landmarks.append(pred[i])
            organ_landmarks = np.array(organ_landmarks, dtype=int)

            print("* * *")
            print(organ_landmarks)
            print("* * *")

        if landmark == "left eye":
            for i in [35, 36, 33, 37, 39, 42, 40, 41, 35]:
                organ_landmarks.append(pred[i])
            organ_landmarks = np.array(organ_landmarks, dtype=int)

        if landmark == "right eye":
            for i in [89, 90, 87, 91, 93, 96, 94, 95]:
                organ_landmarks.append(pred[i])
            organ_landmarks = np.array(organ_landmarks, dtype=int)


        x, y, w, h = cv2.boundingRect(organ_landmarks)
        mask = np.zeros(image.shape, dtype=np.uint8)
        cv2.drawContours(mask, [organ_landmarks], -1, (255, 255, 255), -1)
        mask = mask // 255

        result = image * mask
        result = result [y:y+h, x:x+w]

        result_big = cv2.resize(result, (0, 0), fx=6, fy=6)
        hh, ww, _ = result_big.shape
        
        hhh, www, _ = apple.shape
        lip_loc = [int(hhh//1.7), int(www//2.65)]
        left_eye_loc = [int(hhh//2.3), int(www//2.8)]
        right_eye_loc = [int(hhh//2.3), int(www//1.9)]
        # apple = apple.astype(np.uint8)
        if landmark == "lips":
            for i in range(hh):
                for j in range(ww):
                    if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                        result_big[i][j] = apple[lip_loc[0]+i, lip_loc[1]+j]
            apple[lip_loc[0]:lip_loc[0] + hh, lip_loc[1]:lip_loc[1] + ww] = result_big
            # apple1 = cv2.imread("output/output apple2.jpg")
                            
        if landmark == "left eye":
            for i in range(hh):
                for j in range(ww):
                    if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                        result_big[i][j] = apple[left_eye_loc[0]+i, left_eye_loc[1]+j]
            apple[left_eye_loc[0]:left_eye_loc[0] + hh, left_eye_loc[1]:left_eye_loc[1] + ww] = result_big
            # cv2.imwrite("output/output apple3.jpg", apple1)
        # apple1 = cv2.imread("output/output apple2.jpg")

        if landmark == "right eye":
            for i in range(hh):
                for j in range(ww):
                    if result_big[i][j][0] == 0 and result_big[i][j][1] == 0 and result_big[i][j][2] == 0:
                        result_big[i][j] = apple[right_eye_loc[0]+i, right_eye_loc[1]+j]
            apple[right_eye_loc[0]:right_eye_loc[0] + hh, right_eye_loc[1]:right_eye_loc[1] + ww] = result_big
        
        
        # apple[lip_loc[0]:lip_loc[0] + hh, lip_loc[1]:lip_loc[1] + ww] = result_big
        
    
    print(time.perf_counter() - start_time)

    cv2.imshow("result", result_big)
    cv2.waitKey()
    cv2.imwrite("output/" + landmark + ".jpg", result_big)
    cv2.imwrite("input/apple2.jpg", apple)
    
    return result_big
    

zoom_effect("input\image22.jpg", "lips")
zoom_effect("input\image22.jpg", "left eye")
zoom_effect("input\image22.jpg", "right eye")
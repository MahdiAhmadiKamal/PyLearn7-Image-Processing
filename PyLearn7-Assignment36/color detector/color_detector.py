import cv2
import numpy as np


cap = cv2.VideoCapture(0)
box = np.zeros((110, 110), dtype=int)

while True:
    _, frame = cap.read()
    
    box_col_1 = frame.shape[1]//2 - 55
    box_row_1 = frame.shape[0]//2 - 55
    box_col_2 = frame.shape[1]//2 + 55
    box_row_2 = frame.shape[0]//2 + 55
    
    cv2.rectangle(frame, (box_col_1, box_row_1), (box_col_2, box_row_2), 0, 7)
    box = frame[box_col_1:box_col_2, box_row_1:box_row_2]

    blue = np.count_nonzero(box[:, :, 0] > 120)
    green = np.count_nonzero(box[:, :, 1] > 140)
    red = np.count_nonzero(box[:, :, 2] > 130)


    cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
    
    cv2.imshow("Color Detector", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

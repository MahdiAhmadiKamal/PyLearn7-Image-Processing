import cv2
import numpy as np


cap = cv2.VideoCapture(0)
box = np.zeros((110, 110), dtype=int)

while True:
    _, frame = cap.read()
    frame_hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    box_col_1 = frame.shape[1]//2 - 55
    box_row_1 = frame.shape[0]//2 - 55
    box_col_2 = frame.shape[1]//2 + 55
    box_row_2 = frame.shape[0]//2 + 55
    
    cv2.rectangle(frame, (box_col_1, box_row_1), (box_col_2, box_row_2), 0, 7)
    box = frame_hsv[box_col_1:box_col_2, box_row_1:box_row_2]
    box_area = box.shape[0] * box.shape[1]
    
    H = box[:, :, 0]
    S = box[:, :, 1]
    V = box[:, :, 2]

    S_value = np.sum(S > 50)
    V_value = np.sum(V > 50)
    
    condition_red = (H < 15) | (H > 165) 
    ext = np.extract(condition_red, H)


    if S_value > 0.8 * box_area and V_value > 0.8 * box_area: 
        
        print(np.sum(len(ext)))
        if np.sum(len(ext)) > 0.7 * box_area:
            color = "[red]" 
        else:
            color = ""

        cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
    
    cv2.imshow("Color Detector", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

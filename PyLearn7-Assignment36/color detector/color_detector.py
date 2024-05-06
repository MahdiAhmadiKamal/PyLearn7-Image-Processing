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
    # H = np.count_nonzero(box[:, :, 0] > 120)
    S = np.sum(box[:, :, 1] > 50)
    V = np.sum(box[:, :, 2] > 50)

    # for i in range(box.shape[0]):
    #     for j in range(box.shape[1]):
            # means: if in at least 80% of pixels, S > 50 & V > 50
    if S > 0.8 * box_area and V > 0.8 * box_area: 
        if np.sum( box[:, :, 0] <15 ) > 0.7 * box_area:
            color = "[red]" 
    else:
        color = ""        

    cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
    
    cv2.imshow("Color Detector", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

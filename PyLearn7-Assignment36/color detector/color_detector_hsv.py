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

    S_value = np.sum(S > 40)
    V_value = np.sum(V > 40)
    S_value_for_white = np.sum(S < 10)
    V_value_for_white = np.sum(V > 85)
    V_value_for_black = np.sum(V < 10)

    condition_red = (H < 15) | (H > 165) 
    condition_green = (45 < H) & (H < 85) 
    condition_blue = (105 < H) & (H < 135)
    condition_yellow = (22.5 < H) & (H < 32.5)
    condition_orange = (12.5 < H) & (H < 35)
    condition_purple = (132.5 < H) & (H < 145)

    ext_red = np.extract(condition_red, H)
    ext_green = np.extract(condition_green, H)
    ext_blue = np.extract(condition_blue, H)
    ext_yellow = np.extract(condition_yellow, H)
    ext_orange = np.extract(condition_orange, H)
    ext_purple = np.extract(condition_purple, H)


    if S_value > 0.8 * box_area and V_value > 0.8 * box_area: 
        
        if np.sum(len(ext_red)) > 0.7 * box_area:
            color = "[red]" 
        elif np.sum(len(ext_green)) > 0.7 * box_area:
            color = "[green]" 
        elif np.sum(len(ext_blue)) > 0.7 * box_area:
            color = "[blue]" 
        elif np.sum(len(ext_yellow)) > 0.7 * box_area:
            color = "[yellow]"   
        elif np.sum(len(ext_orange)) > 0.7 * box_area:
            color = "[orange]" 
        elif np.sum(len(ext_purple)) > 0.7 * box_area:
            color = "[purple]"  
        else:
            color = ""

        cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
    
    # if S_value_for_white > 0.8 * box_area and V_value_for_white > 0.8 * box_area: 
    #     color = "[white]"  

    #     cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)

    # if V_value_for_black > 0.8 * box_area: 
    #     color = "[black]"  
        
    #     cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
    
    cv2.imshow("Color Detector", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

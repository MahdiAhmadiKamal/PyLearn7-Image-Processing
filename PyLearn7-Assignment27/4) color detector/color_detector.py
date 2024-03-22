import fractions
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
box = np.zeros((110, 110), dtype=int)

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    box_col_1 = frame.shape[1]//2 - 55
    box_row_1 = frame.shape[0]//2 - 55
    box_col_2 = frame.shape[1]//2 + 55
    box_row_2 = frame.shape[0]//2 + 55
    
    cv2.rectangle(frame, (box_col_1, box_row_1), (box_col_2, box_row_2), 0, 7)
    box = frame[box_col_1:box_col_2, box_row_1:box_row_2]

    b = np.count_nonzero((box < 80))
    g = np.count_nonzero((box > 120) & (box < 160))
    w = np.count_nonzero((box > 150))
    
    if b > 0.7 * (box.shape[0] * box.shape[1]):
        # print("black")
        color = "[black]"
    elif g > 0.7 * (box.shape[0] * box.shape[1]):
        color = "[gray]"
    elif w > 0.7 * (box.shape[0] * box.shape[1]):
        color = "[white]"
    else:
        color = ""

    cv2.putText(frame, color, (box_col_1 - 5, box_row_1 - 15), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)
    
    cv2.imshow("B&W Color Detector", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


# print(frame)
# print(box)
# print(box.shape[0] * box.shape[1])

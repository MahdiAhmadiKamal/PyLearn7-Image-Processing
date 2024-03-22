import fractions
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
box = np.zeros((55, 55), dtype=int)

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    box_col_1 = frame.shape[1]//2 - 55
    box_row_1 = frame.shape[0]//2 - 55
    box_col_2 = frame.shape[1]//2 + 55
    box_row_2 = frame.shape[0]//2 + 55
    
    cv2.rectangle(frame, (box_col_1, box_row_1), (box_col_2, box_row_2), 0, 10)
    box = 

    # for row in range(box_row_1, box_row_2):
    #     for col in range(box_col_1, box_col_2):
    #         c = np.count_nonzero(frame < 100)
    #         if c > 2000:
    #             print("black")


    cv2.imshow("resule", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

print(frame.shape[0])
print(frame.shape[1])


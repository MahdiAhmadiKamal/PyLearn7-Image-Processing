import fractions
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
box = np.zeros((110, 110), dtype=int)

while True:
    _, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    box_col_1 = frame.shape[1]//2 - 55
    box_row_1 = frame.shape[0]//2 - 55
    box_col_2 = frame.shape[1]//2 + 55
    box_row_2 = frame.shape[0]//2 + 55
    
    cv2.rectangle(frame, (box_col_1, box_row_1), (box_col_2, box_row_2), 0, 7)
    box = frame[box_col_1:box_col_2, box_row_1:box_row_2]

    # b, g, r = cv2.split(frame)

    blue = np.count_nonzero(box[:, :, 0] > 120)
    green = np.count_nonzero(box[:, :, 1] > 140)
    red = np.count_nonzero(box[:, :, 2] > 130)

    # b = np.count_nonzero((box < 80))
    # g = np.count_nonzero((box > 120) & (box < 160))
    # w = np.count_nonzero((box > 150))
    
    if blue > 0.7 * (box.shape[0] * box.shape[1]):
        # print("black")
        color = "[blue]"
    elif green > 0.7 * (box.shape[0] * box.shape[1]):
        color = "[green]"
    elif red > 0.7 * (box.shape[0] * box.shape[1]):
        color = "[red]"
    elif red > 0.35 * (box.shape[0] * box.shape[1]) and green > 0.35 * (box.shape[0] * box.shape[1]):
        color = "[yellow]"
    elif red > 0.47 * (box.shape[0] * box.shape[1]) and green > 0.23 * (box.shape[0] * box.shape[1]):
        color = "[orange]"
    elif red > 0.29 * (box.shape[0] * box.shape[1]) and blue > 0.41 * (box.shape[0] * box.shape[1]):
        color = "[purple]"
    elif blue > 0.23 * (box.shape[0] * box.shape[1]) and green > 0.23 * (box.shape[0] * box.shape[1]) and red > 0.23 * (box.shape[0] * box.shape[1]):
        color = "[white]" 
    elif blue < 0.03 * (box.shape[0] * box.shape[1]) and green < 0.03 * (box.shape[0] * box.shape[1]) and red < 0.03 * (box.shape[0] * box.shape[1]):
        color = "[black]"   
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

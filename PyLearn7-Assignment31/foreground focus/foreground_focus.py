import numpy as np
import cv2


image = cv2.imread("input/flower_input.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
result = np.zeros((rows, cols), dtype=np.uint8)

filter = np.ones((11, 11), dtype=np.float32)/121
          
for i in range(5, rows-5):
    for j in range(5, cols-5):
        
        if image[i,j] < 150:
            region = image[i-5:i+6, j-5:j+6]
            result[i, j] = np.abs(np.sum(filter * region))
        else:
            result[i, j] = image [i, j]

cv2.imwrite("output/flower_output.png", result)
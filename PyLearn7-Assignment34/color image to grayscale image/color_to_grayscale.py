import cv2
import numpy as np

def pycolor2gray(image):
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rows, cols, _ = image.shape

    R, G, B = cv2.split(image)

    result = np.zeros((rows, cols), dtype=np.uint8)

    for row in range(rows):
        for col in range(cols):
            result[row, col] = R[row, col]//3 + G[row, col]//3 + B[row, col]//3

    cv2.imshow("", result)
    cv2.waitKey(0)
    return result


image = cv2.imread("input/macaw.jpg")
gray_image = pycolor2gray(image)
cv2.imwrite("output/gray image.jpg", gray_image)
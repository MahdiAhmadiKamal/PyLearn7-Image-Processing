import numpy as np
import cv2


def edge_detection(image, direction):
    rows, cols = image.shape
    result = np.zeros((rows, cols), dtype=np.uint8)

    if direction == "horizontal":
        filter = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]])
    if direction == "vertical":
        filter = np.array([[2, 0, -2],
                            [2, 0, -2],
                            [2, 0, -2]])
            
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            region = image[i-1:i+2, j-1:j+2]
            result[i, j] = np.abs(np.sum(filter * region))

    return result

img = cv2.imread("input/building.tif", cv2.IMREAD_GRAYSCALE)

h_img = edge_detection(img, "horizontal")
cv2.imwrite("output/h_img.png", h_img)

v_img = edge_detection(img, "vertical")
cv2.imwrite("output/v_img.png", v_img)
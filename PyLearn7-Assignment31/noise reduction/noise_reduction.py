import numpy as np
import cv2


def noise_reduction(image, dim):
    rows, cols = image.shape
    result = np.zeros((rows, cols), dtype=np.uint8)

    filter = np.ones((dim, dim)) / (dim * dim)
    margin = dim // 2
            
    for i in range(margin, rows-margin):
        for j in range(margin, cols-margin):

            region = image[i-margin:i+margin+1, j-margin:j+margin+1]
            average = np.sum(filter * region)
            result[i, j] = average

    return result

img = cv2.imread("input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)

result = noise_reduction(img, 15)
cv2.imwrite("output/xray_noisy_15x15.png", result)


import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread("input/2-black-white-secrets.jpg", cv2.IMREAD_GRAYSCALE)
histogram = []
rows, cols = image.shape
# print(image.shape)
for num in range(0, 256):
    count = 0
    for i in range(rows):
        for j in range(cols):
            pixel = image[i, j]
            if pixel == num:
                count += 1
    histogram.append(count)

# print(histogram)
plt.plot(histogram)
plt.show()
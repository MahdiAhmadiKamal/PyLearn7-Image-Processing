import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread("input/image_2.jpg", cv2.IMREAD_GRAYSCALE)

def histogram(image):

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
    return histogram

histo = histogram(image)
plt.plot(histo)
plt.show()
plt.hist(image.ravel(), 256)
plt.show()
plt.bar(np.arange(256), histo)
plt.show()

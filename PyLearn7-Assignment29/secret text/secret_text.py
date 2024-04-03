import cv2
import numpy as np


image_1 = cv2.imread("input/image 1.jpg")
image_2 = cv2.imread("input/image 2.jpg")

result = cv2.subtract(image_2, image_1)

cv2.imwrite("output/result.jpg", result)
import os
import cv2
import numpy as np


image_leo = cv2.imread("input/Brad.jpg")
image_brad = cv2.imread("input/Leonardo.jpg")

image_leo = cv2.cvtColor(image_leo, cv2.COLOR_BGR2GRAY)
image_brad = cv2.cvtColor(image_brad, cv2.COLOR_BGR2GRAY)

image_leo = image_leo.astype(np.float32)
image_brad = image_brad.astype(np.float32)

result = (image_leo + image_brad) / 2
result = result.astype(np.uint8)

cv2.imwrite("output/result.jpg", result)
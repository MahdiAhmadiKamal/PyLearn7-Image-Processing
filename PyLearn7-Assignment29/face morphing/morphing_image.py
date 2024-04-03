# import os
# from re import X
# from turtle import xcor
import cv2
import numpy as np


image_start = cv2.imread("input/young.jpg")
image_end = cv2.imread("input/old.jpg")

# image_leo = cv2.cvtColor(image_leo, cv2.COLOR_BGR2GRAY)
# image_brad = cv2.cvtColor(image_brad, cv2.COLOR_BGR2GRAY)

image_end = image_end.astype(np.float32)
image_start = image_start.astype(np.float32)

step_1 = (image_start*3/4 + image_end*1/4)
step_2 = (image_start*2/4 + image_end*2/4)
step_3 = (image_start*1/4 + image_end*3/4)

result = np.concatenate((image_start, step_1, step_2, step_3, image_end), axis=1)
result = result.astype(np.uint8)
cv2.imwrite("output/result2.jpg", result)
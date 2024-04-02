import os
from re import X
from turtle import xcor
import cv2
import numpy as np


image_leo = cv2.imread("input/ab1.jpg")
image_brad = cv2.imread("input/ab2.jpg")

# image_leo = cv2.cvtColor(image_leo, cv2.COLOR_BGR2GRAY)
# image_brad = cv2.cvtColor(image_brad, cv2.COLOR_BGR2GRAY)

image_leo = image_leo.astype(np.float32)
image_brad = image_brad.astype(np.float32)


step_1 = (image_leo*3/4 + image_brad*1/4)
step_2 = (image_leo*2/4 + image_brad*2/4)
step_3 = (image_leo*1/4 + image_brad*3/4)

result = np.concatenate((image_brad, step_3, step_2, step_1, image_leo), axis=1)
result = result.astype(np.uint8)
cv2.imwrite("output/result.jpg", result)
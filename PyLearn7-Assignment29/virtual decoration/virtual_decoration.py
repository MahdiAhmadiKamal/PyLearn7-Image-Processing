import cv2
import numpy as np

image_room = cv2.imread("input/vd1.jpg")
image_floor = cv2.imread("input/vd2.jpg")
image_mask_1 = cv2.imread("input/vd3.jpg")

image_mask_2 = 255 - image_mask_1
cv2.imwrite("output/new_mask.jpg", image_mask_2)


image_mask_1 = image_mask_1 / 255.0
image_mask_2 = image_mask_2 / 255.0

result_1 = image_floor * image_mask_1
cv2.imwrite("output/floor.jpg", result_1)

result_2 = image_room * image_mask_2
cv2.imwrite("output/furniture.jpg", result_2)

result = result_1 + result_2

cv2.imwrite("output/room.jpg", result)


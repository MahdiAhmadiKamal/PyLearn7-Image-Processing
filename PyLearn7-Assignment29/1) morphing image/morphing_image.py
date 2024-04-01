import os
import cv2
import numpy as np


image_leo = cv2.imread("input/Brad.jpg")
image_brad = cv2.imread("input/Leonardo.jpg")

image_leo = cv2.cvtColor(image_leo, cv2.COLOR_BGR2GRAY)
image_brad = cv2.cvtColor(image_brad, cv2.COLOR_BGR2GRAY)
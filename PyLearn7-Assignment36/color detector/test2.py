import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.array([[203, 192, 182],
                [200, 55, 66],
                [45, 88, 77],
                [8, 42, 179],
                [8, 16, 10]])

con = (image>200) | (image<15)
ext = np.extract(con,image)
print(ext)

c = np.sum(len(ext))
print(c)


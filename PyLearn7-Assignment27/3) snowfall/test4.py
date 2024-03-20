import cv2
import numpy as np

background_image = np.random.randint(6, size=(5, 5))
snow_image = np.ones_like(background_image) * 255

print(background_image)
print(snow_image)
print(cv2.add(background_image, snow_image))
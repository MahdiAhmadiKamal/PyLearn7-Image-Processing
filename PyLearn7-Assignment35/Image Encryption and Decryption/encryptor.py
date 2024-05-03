import cv2
import numpy as np


img = cv2.imread("input/Mona Lisa.jpg")

secret_key = np.random.randint(0, 256, (img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
np.save('output/secret_key.npy', secret_key)

img_encrypted = cv2.bitwise_xor(img, secret_key)
cv2.imwrite('output/encrypted_image.bmp', img_encrypted)

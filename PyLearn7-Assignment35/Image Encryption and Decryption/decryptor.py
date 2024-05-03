import cv2
import numpy as np


cipher_img = cv2.imread("enc_output/encrypted_image.bmp")
secret_key = np.load("enc_output\secret_key.npy")

img_decrypted = cv2.bitwise_xor(cipher_img, secret_key)

cv2.imwrite('dec_output/decrypted_image.jpg', img_decrypted)
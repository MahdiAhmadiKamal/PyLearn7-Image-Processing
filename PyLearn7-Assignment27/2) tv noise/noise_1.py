import cv2
import numpy as np

theme_image = cv2.imread("image1.png")
theme_image = cv2.cvtColor(theme_image, cv2.COLOR_BGR2GRAY)

rows = theme_image.shape[0]
cols = theme_image.shape[1]

writer = cv2.VideoWriter("output_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (cols, rows))

while True:
    noise_image = np.random.random((61, 61)) * 255
    noise_image = np.array(noise_image, dtype=np.uint8)

    theme_image[57:118, 80:141] = noise_image
    writer.write(theme_image)
    cv2.imshow("noise", theme_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()
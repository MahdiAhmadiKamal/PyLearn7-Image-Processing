import cv2
import numpy as np
import imageio


image = cv2.imread("image1.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rows = image.shape[0]
cols = image.shape[1]

writer = cv2.VideoWriter("output_video1.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

frames = []
while True:
    noise_image = np.random.random((61, 61)) * 255
    noise_image = np.array(noise_image, dtype=np.uint8)

    image[57:118, 80:141] = noise_image

    new_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    frames.append(new_image)

    writer.write(new_image)
    cv2.imshow("noise", new_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

imageio.mimsave ("output_gif1.gif", frames)
writer.release()

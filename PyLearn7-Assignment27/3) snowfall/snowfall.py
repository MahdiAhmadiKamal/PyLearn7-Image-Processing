import cv2
import numpy as np
import imageio


image = cv2.imread("image1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

snow_intensity = 100
snowflake_size = 2

rows = image.shape[0]
cols = image.shape[1]

writer = cv2.VideoWriter("output_video1.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

frames = []
while True:

    snow = np.zeros_like(image)
    
    for i in range(snow_intensity):
        x = np.random.randint(0, cols)
        y = np.random.randint(0, rows)
        cv2.circle(snow, (x, y), snowflake_size, 255, -1)
       
    snowy_image = cv2.add(image, snow)
    new_snowy_image = cv2.cvtColor(snowy_image, cv2.COLOR_BGR2RGB)

    frames.append(new_snowy_image)

    writer.write(new_snowy_image)
    cv2.imshow("snowfall", new_snowy_image)
    if cv2.waitKey(250) & 0xFF == ord('q'):
        break

imageio.mimsave ("output_gif.gif", frames)
writer.release()

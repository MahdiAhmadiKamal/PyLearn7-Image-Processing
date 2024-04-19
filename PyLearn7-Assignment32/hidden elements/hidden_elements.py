import numpy as np
import cv2


image = cv2.imread("input/1.tif")

avg_filter1 = np.ones((5, 5), dtype=np.float32) * 0.04
avg_filter2 = np.ones((5, 5), dtype=np.float32)
avg_filter3 = np.ones((5, 5), dtype=np.float32) * 5
avg_filter4 = np.ones((3, 3), dtype=np.float32) * 0.04
avg_filter5 = np.ones((3, 3), dtype=np.float32)
avg_filter6 = np.ones((3, 3), dtype=np.float32) * 5

filters = [avg_filter1, avg_filter2, avg_filter3, avg_filter4, avg_filter5, avg_filter6]

i = 1
for filter in filters:
    
    result = cv2.filter2D(image, -1, filter)
    result = np.hstack([image, result])
    cv2.imwrite("output/result" + str(i) + ".jpg", result)
    i += 1


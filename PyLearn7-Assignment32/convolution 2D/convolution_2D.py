import cv2
import numpy as np


image = cv2.imread("input/butterfly.webp")

# 1. Edge detection filter
kernel1 = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])

# 2. Sharpening filter
kernel2 = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

# 3. Emboss filter
kernel3 = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 4. Identity filter
kernel4 = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

# 5. My filter
kernel5 = np.array([[1  ,  1 ,  1],
                   [0  ,  1 ,  1],
                   [0  ,  0 ,  1]])

# 6. My filter
kernel6 = np.array([[1  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  1]])

# 7. My filter
kernel7 = np.array([[0  ,  1 ,  0],
                   [-1  ,  0 ,  1],
                   [0  ,  -1 ,  0]])

kernels = [kernel1, kernel2, kernel3, kernel4, kernel5, kernel6, kernel7]

i = 1
for kernel in kernels:
    
    result = cv2.filter2D(image, -1, kernel)
    result = np.hstack([image, result])
    cv2.imwrite("output/result_" + str(i) + ".jpg", result)
    i += 1
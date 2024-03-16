import numpy as np
from scipy.ndimage import rotate

x = np.random.randint(800, 1000, size=[100, 100, 3])
rotated = rotate(x, angle=45)
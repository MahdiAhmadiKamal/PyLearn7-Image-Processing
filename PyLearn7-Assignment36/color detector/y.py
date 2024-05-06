import numpy as np


list = [203, 192, 182, 192, 210, 219, 224, 226, 226, 227]
# list = [1, 2, 3, 3, 3, 4, 5, 6]
c = sum(list.count(2<i<200) for i in str(list))print(c)
from math import floor
from typing import List

import numpy as np


def imageSmoother(M: List[List[int]]):
    M = np.array(M)
    shape = M.shape
    row = shape[0]
    col = shape[1]
    empty = np.zeros(shape)

    return 0


a = [[1, 1, 1],
     [1, 0, 1]]
a = np.array(a)
print(a.shape)

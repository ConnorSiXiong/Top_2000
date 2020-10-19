from typing import List

import numpy as np


def diagonalSum(mat: List[List[int]]) -> int:
    if len(mat) == 1:
        return mat[0][0]

    side = len(mat)

    left = np.diag(mat)
    right = np.diag(np.fliplr(mat))

    res = sum(left) + sum(right)

    if side % 2 == 0:
        return res
    else:
        return res - mat[int((side + 1) / 2)][int((side + 1) / 2)]


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalSum(a))

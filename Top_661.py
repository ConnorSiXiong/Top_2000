from math import floor
from typing import List

import numpy as np


def imageSmoother(M: List[List[int]]):
    M = np.array(M)
    shape = M.shape
    row = shape[0]
    col = shape[1]

    empty = np.zeros(shape)

    # 单行的情况
    if row == 1:
        if col <= 2:
            val = np.average(M)
            empty = np.full(shape, val, dtype=int)
            return empty.tolist()
        else:
            for j in range(col):
                if j == 0:
                    empty[0][j] = floor((M[0][0] + M[0][1]) / 2)
                elif j == col - 1:
                    empty[0][j] = floor((M[0][j] + M[0][j - 1]) / 2)
                else:
                    empty[0][j] = floor((M[0][j - 1] + M[0][j] + M[0][j + 1]) / 3)
            empty = empty.astype(int)
            return empty.tolist()

    # 单列的情况
    if col == 1:
        if row <= 2:
            val = np.average(M)
            empty = np.full(shape, val, dtype=int)
            return empty.tolist()
        else:
            for i in range(row):
                if i == 0:
                    empty[i][0] = floor((M[0][0] + M[1][0]) / 2)
                elif i == row - 1:
                    empty[i][0] = floor((M[i - 1][0] + M[i][0]) / 2)
                else:
                    empty[i][0] = floor((M[i - 1][0] + M[i][0] + M[i + 1][0]) / 3)
            empty = empty.astype(int)
            return empty.tolist()

    # 非单行或单列的情况
    for i in range(row):
        for j in range(col):
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                if i == 0:
                    if j == 0:
                        empty[i][j] = floor((M[i][j] + M[i][j + 1] + M[i + 1][j] + M[i + 1][j + 1]) / 4)
                    elif j == col - 1:
                        empty[i][j] = floor((M[i][j] + M[i + 1][j] + M[i][j - 1] + M[i + 1][j - 1]) / 4)
                    else:
                        empty[i][j] = floor(
                            (M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) / 6)

                elif i == row - 1:
                    if j == 0:
                        empty[i][j] = floor((M[i][j] + M[i][j + 1] + M[i - 1][j] + M[i - 1][j + 1]) / 4)
                    elif j == col - 1:
                        empty[i][j] = floor((M[i][j] + M[i][j - 1] + M[i - 1][j] + M[i - 1][j - 1]) / 4)
                    else:
                        empty[i][j] = floor(
                            (M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1]) / 6)

                elif j == 0:
                    empty[i][j] = floor(
                        (M[i - 1][j] + M[i][j] + M[i + 1][j] + M[i - 1][j + 1] + M[i][j + 1] + M[i + 1][j + 1]) / 6)
                elif j == col - 1:
                    empty[i][j] = floor(
                        (M[i - 1][j] + M[i][j] + M[i + 1][j] + M[i - 1][j - 1] + M[i][j - 1] + M[i + 1][j - 1]) / 6)

            else:
                # 一起有9个格子
                empty[i][j] = floor((M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j - 1] + M[i][j] + M[i][
                    j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) / 9)
    empty = empty.astype(int)
    return empty.tolist()


a = [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]

b = [[1]]

c = [[1, 10, 1]]
print(imageSmoother(a))

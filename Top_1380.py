from typing import List

import numpy as np


def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    res = []
    matrix = np.array(matrix)

    for i in range(len(matrix)):
        min_col_index = np.argmin(matrix[i])
        max_row_index = np.argmax(matrix[:, min_col_index])
        if max_row_index == i:
            res.append(np.min(matrix[i]))
    return res


def luckyNumbers2(matrix: List[List[int]]) -> List[int]:
    res = []
    rows = len(matrix)
    for i in range(rows):
        min_in_row = min(matrix[i])
        min_col_index = matrix[i].index(min_in_row)
        if min_in_row == max([matrix[j][min_col_index] for j in range(rows)]):
            res.append(min_in_row)
    return res

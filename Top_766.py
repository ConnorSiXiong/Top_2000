from typing import List


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 1 or cols == 1:
        return True

    # 第一列
    for i in range(cols):
        a = 0
        b = i
        anchor = matrix[a][b]
        while b < cols and a < rows:
            next_one = matrix[a][b]
            # print(next_one)
            if next_one != anchor:
                return False
            b += 1
            a += 1

    # 第一行
    for i in range(1, rows):
        a = i
        b = 0
        anchor = matrix[a][b]
        while b < cols and a < rows:
            next_one = matrix[a][b]

            if next_one != anchor:
                return False
            b += 1
            a += 1
    return True


matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
#
# matrix = [
#   [1,2],
#   [2,2]
# ]

print(isToeplitzMatrix(matrix))

from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])

    result = 0

    def isSq(i: int, j: int, l: int) -> bool:
        if i + l > rows or j + l > cols:
            return False

        for x in range(i, i + l):
            for y in range(j, j + l):
                if int(matrix[x][y]) != 1:
                    return False

        return True

    for i in range(rows):
        for j in range(cols):
            cur = matrix[i][j]
            if int(cur) == 1:
                l = 1
                while isSq(i, j, l):
                    result = max(result, l * l)
                    l += 1

    return result


a = [[0]]
print(maximalSquare(a))

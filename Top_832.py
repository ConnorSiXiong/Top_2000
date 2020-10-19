from typing import List


def flipAndInvertImage(A: List[List[int]]) -> List[List[int]]:
    a = A
    for row in range(len(A)):
        for col in range(len(A[0])):
            if a[row][col] == 1:
                a[row][col] = 0
            else:
                a[row][col] = 1

    res = []
    for row in a:
        row.reverse()
        res.append(row)

    return res

a = [[1,1,0],[1,0,1],[0,0,0]]
flipAndInvertImage(a)


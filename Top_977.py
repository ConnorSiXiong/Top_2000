from typing import List


def sortedSquares(A: List[int]) -> List[int]:
    for i in range(len(A)):
        A[i] = A[i] ** 2

    return sorted(A)
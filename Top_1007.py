from collections import Counter
from typing import List


def minDominoRotations(A: List[int], B: List[int]) -> int:
    """
    2 <= A.length == B.length <= 2 * 10^4
    1 <= A[i], B[i] <= 6
    """

    if len(A) == 1:
        if A == B:
            return 0
        else:
            return -1

    pre_check_a = [A[i] for i in range(len(A)) if A[i] == B[i]]

    if len(pre_check_a) != 0 and len(set(pre_check_a)) != 1:
        return -1

    a = [A[i] for i in range(len(A)) if A[i] != B[i]]
    b = [B[i] for i in range(len(A)) if A[i] != B[i]]

    max_len = len(a)

    if max_len == 0:
        if len(set(A)) != 1:
            return -1
        else:
            return 0

    a_counter = Counter(a)
    b_counter = Counter(b)

    all_counter = a_counter + b_counter

    candidates = []
    for key, value in all_counter.items():
        if value >= max_len:
            candidates.append(key)

    candidates2 = []
    for i in candidates:
        candidates2.append(max_len - max(a_counter.get(i), b_counter.get(i)))

    if candidates2:
        return max(candidates2)
    else:
        return -1


A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]
# A = [3, 5, 1, 2, 3]
# B = [3, 6, 3, 3, 4]
# A = [1,1,-1]
# B = [1,1,-1]

# A = [2,3,2,1,1,1,2,2]
# B = [2,1,2,1,1,3,1,1]

A = [1, 2, 3, 4, 6]
B = [6, 6, 6, 6, 5]
print(minDominoRotations(A, B))

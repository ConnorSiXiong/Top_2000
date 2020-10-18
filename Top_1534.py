from typing import List


def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
    box = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                v_i = arr[i]
                v_j = arr[j]
                v_k = arr[k]

                if abs(v_i - v_j) <= a and abs(v_j - v_k) <= b and abs(v_i - v_k) <= c:
                    box.append((v_i, v_j, v_k))
    return len(box)


a = [3, 0, 1, 1, 9, 7]
print(countGoodTriplets(a, 7, 2, 3))

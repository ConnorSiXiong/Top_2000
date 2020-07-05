from typing import List


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr = sorted(arr)
    if len(arr) == 2:
        return True
    dif = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != dif:
            return False
    return True

arr = [2,4,1]
print(canMakeArithmeticProgression(arr))
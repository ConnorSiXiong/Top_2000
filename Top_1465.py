from typing import List


def maxArea(h: int, w: int, arr1: List[int], arr2: List[int]) -> int:
    arr1 = [0] + arr1 + [h]
    arr2 = [0] + arr2 + [w]
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    max1 = 0
    max2 = 0

    for i in range(1, len(arr1)):
        max1 = max(arr1[i] - arr1[i - 1], max1)
    for i in range(1, len(arr2)):
        max2 = max(arr2[i] - arr2[i - 1], max2)

    return max1 * max2 % (1000000000 + 7)

h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [3,1]

print(maxArea(h,w,horizontalCuts,verticalCuts))

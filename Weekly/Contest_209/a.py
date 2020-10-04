from typing import List


def specialArray(nums: List[int]) -> int:
    for i in range(1001):
        res = 0
        for x in nums:
            if x >= i:
                res += 1
        if res == i:
            return res

    return -1


a1 = [3, 5]
a2 = [0, 0]
a3 = [0, 4, 3, 0, 4]
a4 = [3, 6, 7, 7, 0]
a5 = [1, 1, 5, 5]
a6 = [3, 3, 3]
a7 = [0, 0, 0, 1]
print(specialArray(a7))

from typing import List


def specialArray(nums: List[int]) -> int:
    for candidate in range(101):
        count = 0
        for i in nums:
            if i >= candidate:
                count += 1
        if count == candidate:
            return count
    return -1


a1 = [3, 5]
a2 = [0, 0]
a3 = [0, 4, 3, 0, 4]
a4 = [3, 6, 7, 7, 0]
a5 = [1, 1, 5, 5]
a6 = [3, 3, 3]
a7 = [0, 0, 0, 1]
print(specialArray(a2))

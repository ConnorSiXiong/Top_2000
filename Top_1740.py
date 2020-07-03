from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:

    l = len(nums)
    result = []
    a1 = 0
    a2 = n
    while a2 < l:
        result.append(nums[a1])
        result.append(nums[a2])
        a1 += 1
        a2 += 1
    return result


a = [2, 5, 1, 3, 4, 7]
#   [2,3,5,4,1,7]

print(shuffle(a, 3))

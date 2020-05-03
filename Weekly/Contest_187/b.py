from typing import List


def kLengthApart(nums: List[int], k: int) -> bool:
    l = len(nums)
    min_gap = l + 1

    if l == 1:
        return False
    # k == 0 是两个 1 相邻

    anchor_one_index = 0

    # find the first one
    one_occurs = 0

    while True:
        if anchor_one_index == l:
            return False
        if nums[anchor_one_index] == 1:
            one_occurs += 1
            break
        anchor_one_index += 1

    for i in range(anchor_one_index + 1, l):
        if nums[i] == 1:
            one_occurs += 1
            min_gap = min(min_gap, i - anchor_one_index - 1)
            anchor_one_index = i

    if one_occurs == 1:
        return True

    return min_gap >= k

def kLengthApart2(nums: List[int], k: int) -> bool:
    l = len(nums)
    anchor_one_index = -l
    for i in range(len(nums)):
        if nums[i] == 1:
            gap = i - anchor_one_index - 1
            if gap < k:
                return False
            anchor_one_index = i
    return True
nums = [0,0,0]
k = 1
print(kLengthApart(nums, k))
print(kLengthApart2(nums, k))

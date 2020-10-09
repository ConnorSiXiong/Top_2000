from typing import List


def search(nums: List[int], target: int) -> int:
    for i in range(len(nums)):

        if nums[i] == target:
            return i
    return -1


def search2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


a = [-1, 2]
target0 = -1
result = search2(a, target0)
print(result)



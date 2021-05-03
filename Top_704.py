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
"""
    使用新办法
    - 复习
    2021-05-03
    20:37 - 20:41
"""


def search3(arr, target):
    if not arr:
        return -1
    if target > arr[-1] or target < arr[0]:
        return -1

    left = 0
    right = len(arr)

    while left + 1 < right:
        mid = (left + right) // 2

        if target < arr[mid]:
            right = mid
        else:
            left = mid

    if arr[left] == target:
        return left
    if arr[right] == target:
        return right
    return -1


print(search3([-1, 0, 3, 5, 9, 12], 2))

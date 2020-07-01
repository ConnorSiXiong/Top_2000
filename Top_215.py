from typing import List
import random


def findKthLargest(nums: List[int], k: int) -> int:
    def partition(arr: List[int], left: int, right: int) -> int:
        index = random.randint(right-left, right)
        temp = arr[index]
        arr[index] = arr[left]
        arr[left] = temp

        flag = arr[left]
        j = left
        for i in range(left + 1, right + 1):
            if arr[i] < flag:
                j += 1
                temp = arr[i]
                arr[i] = arr[j]

                arr[j] = temp
        temp = arr[j]
        arr[j] = arr[left]
        arr[left] = temp
        return j

    n = len(nums)
    target = n - k
    left = 0
    right = n - 1
    while True:
        index = partition(nums, left, right)
        if index == target:
            return nums[index]
        elif index < target:
            left = index + 1
        elif index > target:
            right = index - 1

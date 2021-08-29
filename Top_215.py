from typing import List
import random


def findKthLargest(nums: List[int], k: int) -> int:
    def partition(arr: List[int], left: int, right: int) -> int:
        index = random.randint(0, right-left) + left
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

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        pivot = random.choice(nums)

        left = [i for i in nums if i < pivot]
        mid = [i for i in nums if i == pivot]
        right = [i for i in nums if i > pivot]

        r = len(right)
        m = len(mid)

        if k <= r:
            return self.findKthLargest(right, k)
        elif k > r + m:
            return self.findKthLargest(left, k-r-m)
        else:
            return mid[0]
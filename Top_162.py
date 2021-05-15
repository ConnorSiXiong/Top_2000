from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [float('-inf')] + nums + [float('-inf')]
        if (n == 1): return 0
        l = 1
        r = n
        while (l <= r):
            mid = l + (r - l) // 2
            curr = nums[mid]
            left = nums[mid - 1]
            right = nums[mid + 1]
            if (curr > left and curr > right):
                return mid - 1
            elif (curr > left and curr < right):
                l = mid + 1
            elif (curr < left and curr > right):
                r = mid - 1
            else:
                l = mid + 1
        return 0


a = Solution()

print(a.findPeakElement([1, 1, 1]))


def findPeckElement(arr):
    if len(arr) == 0:
        return 0

    left = 1
    right = len(arr) - 2
    arr = [float('-inf')] + arr + [float('-inf')]  # must have this, because [1, 2] return 0
    while left + 1 < right:
        mid = (left + right) // 2
        # if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
        #     return mid
        if arr[mid] < arr[mid + 1]:
            left = mid
        # elif arr[mid] > arr[mid-1]:
        #     right = mid
        else:
            right = mid

    # return left if arr[left] > arr[right] else right
    # because arr = [float('-inf')] + arr + [float('-inf')], so the final res should - 1
    return left - 1 if arr[left] > arr[right] else right - 1


print(float('inf'))

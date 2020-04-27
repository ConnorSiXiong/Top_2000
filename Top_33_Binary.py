from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        mid_value = nums[mid]
        right_value = nums[right]
        left_value = nums[left]

        if mid_value == target:
            return mid
        if right_value == target:
            return right

        if mid_value > right_value:
            if left_value <= target < mid_value:
                # 这里如果分析 mid的右边，有两种情况，比较绕；所以分析左边
                # 第一种情况 4 5 6 8 1 2   target = 8
                # 另一种情况 4 5 6 0 1 2   target = 1
                right = mid - 1
            else:
                left = mid + 1
        else:
            if right_value >= target > mid_value:
                left = mid + 1
            else:
                right = mid - 1
    return -1


a = [5, 6, 0, 1, 2, 3]
t = 1

b = [1]

print(search(a, 3))


def search2(nums: List[int], target: int) -> int:
    pass
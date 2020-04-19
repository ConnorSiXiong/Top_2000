from typing import List


def findMin(nums: List[int]) -> int:

    for i in range(1, len(nums)):
        if nums[i] < nums [i - 1]:
            return nums[i]
    return nums[0]


# 最小值在 mid 的右侧
# [4,5,6,7,0,1,2]

# 最小值在 mid 的左侧
# [6,7,0,1,2,3,4]

def findMin2(nums: List[int]) -> int:
    """
    这个解法跟其他的解法不一样
    它总是在比较nums[-1]
    而不是拿中间值去比较
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        print('mid ', mid)
        if nums[mid] <= nums[-1]:
            right = mid - 1
        else:
            left = mid + 1
    return nums[left]


def findMin3(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2
        # mid = left + (right - left) // 2
        print('mid ', mid)
        if nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid + 1
        # if nums[mid] > nums[right]:
        #     left = mid + 1
        # else:
        #     right = mid
    return nums[left]

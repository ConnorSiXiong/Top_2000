def searchRange(nums, target):
    # Write your code here.
    if target < nums[0] or target > nums[-1]:
        return [-1, -1]

    first_index = findIndex(nums, target)
    if nums[first_index] != target:
        return [-1, -1]
    second_index = findIndex(nums, target + 1)

    return [first_index, second_index-1]


def findIndex( nums, target):
    # xxxooo
    left = 0
    right = len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid
        else:
            right = mid

    if nums[left] >= target:
        return left
    if nums[right] >= target:
        return right
    return -1

print(searchRange([5,7,7,8,8,10], 8))
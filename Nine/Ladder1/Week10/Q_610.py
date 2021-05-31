def twoSum7(nums, target):
    res = [-1, -1]
    i = 0
    j = 1
    target = abs(target)
    while i < len(nums) - 1 and j < len(nums):
        if nums[j] - nums[i] > target:
            if i + 1 == j:
                i += 1
                j += 1
            else:
                i += 1
        elif nums[j] - nums[i] == target:
            return [nums[i], nums[j]]
        else:
            j += 1
    return res


nums = [2, 9, 15, 16]
target = 6
print(twoSum7(nums, target))

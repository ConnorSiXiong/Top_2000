def longestConsecutive(nums):
    # 这个解法首先sort了
    # 其实时间复杂度就超了，不好
    if not nums:
        return 0
    nums = sorted(nums)
    res = 1
    temp = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] - nums[i - 1] == 1:
            temp += 1
        else:
            temp = 1
        res = max(res, temp)
    return res


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [100, 4, 200, 1, 3, 2]
nums = [1, 2, 0, 1]
nums = [0, 0, 0, 0, 0, 1]
print(longestConsecutive(nums))

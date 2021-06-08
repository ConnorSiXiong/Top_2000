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


def longestConsecutive2(nums):
    # 边界考虑

    # 1. 空数组
    # 2. 一个位置的数组
    # 3. 相邻重复怎么算？

    # 我上面那个解法是从1开始计数
    # 这种从1开始计数的这是我第一次做到

    set_nums = set(nums)

    res = 0
    for i in nums:
        if i-1 not in set_nums:
            temp = 1
            while i + 1 in set_nums:
                temp += 1
                i += 1
            res = max(res, temp)
    return res

print(longestConsecutive2(nums))

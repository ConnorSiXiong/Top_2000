# 这个题如果不用双指针会超时
# 关键在 13 行
def twoSum5(self, nums, target):
    nums.sort()

    res = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            res += (right - left)
            left += 1
            right = len(nums) - 1
    return res
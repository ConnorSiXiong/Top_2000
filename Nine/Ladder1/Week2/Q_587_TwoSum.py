class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) <= 1:
            return 0

        left = 0
        right = len(nums) - 1
        nums = sorted(nums)
        res = 0

        while left < right:
            if nums[left] + nums[right] == target:
                res += 1
                left += 1
                right -= 1

            # while left < right and nums[left] == nums[left - 1]:
            #     left += 1
            # while left < right and nums[right] == nums[right + 1]:
            #     right -= 1

            # 之前写成上面这样了，如果在外层的话，那么可能会出现越界
            # 在 == target之后，直接紧接着判断是否存在连续相等
            # 这个注意一下
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            if nums[left] + nums[right] > target:
                right -= 1
            if nums[left] + nums[right] < target:
                left += 1

        return res

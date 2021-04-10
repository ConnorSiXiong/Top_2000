class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):

        self.sort1(nums)

    def sort1(self, nums):
        if len(nums) == 0:
            return None

        self.sort2(nums, 0, len(nums) - 1)

    def sort2(self, nums, start, end):
        if start >= end:
            return

        left = start
        right = end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and pivot > nums[left]:
                left += 1
            while left <= right and pivot < nums[right]:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.sort2(nums, start, right)
        self.sort2(nums, left, end)

#
# a = Solution()
# a.sortColors([2, 0, 0, 1, 2, 0, 2])
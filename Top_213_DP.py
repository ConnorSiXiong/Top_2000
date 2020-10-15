from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) >= 3:
        money_0 = 0
        for i in range(0, len(nums) - 1, 2):
            print('nums[i]', nums[i])
            money_0 += nums[i]
        print('------')
        money_1 = 0
        for i in range(1, len(nums), 2):

            print('nums[i]', nums[i])
            money_1 += nums[i]
        return max(money_0, money_1)
    else:
        return max(nums)

a = [1,3,1,3,100]
print(rob(a))
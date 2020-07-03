from typing import List


def runningSum(nums: List[int]) -> List[int]:
    # [1,2,3,4]
    # [1,3,6,10]
    sum0 = 0

    n = len(nums)

    for i in range(n):
        sum0 += nums[i]
        nums[i] = sum0
    return nums


a = [1,2,3,4]
print(runningSum(a))
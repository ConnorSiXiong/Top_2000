from typing import List


def canJump(nums: List[int]) -> bool:
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        current_max = i + n
        reach = max(reach, current_max)
    return True


def canJump2(nums: List[int]) -> bool:
    """
    每次只往前走一步
    """
    dp = [True] + [False] * (len(nums) - 1)
    for i in range(1, len(nums)):
        print('dp =', dp)
        print('----------')
        print('i =', i)
        for j in range(i)[::-1]:
            print('j =', j)
            if i - j <= nums[j] and dp[j]:
                dp[i] = True
                break
    print('dp =', dp)
    return dp[-1]


a = [2, 3, 1, 1, 4]

b = [3, 2, 1, 0, 4]

c = [1, 3, 0, 0, 0]

d = [1, 1, 8, 0, 0]

print(canJump2(d))

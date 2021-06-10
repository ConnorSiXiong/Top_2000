from typing import List
from collections import deque

"""
这个题目的意思就是

每次可以从位置i往的范围 [i+1, i+k] 跳一步，然后停留在这个位置j上

再从j开始往后范围 [j+1, j+k] 里跳一步

重复

具体例子：
arr = [1, -1, -2, -4, 7, -3, -2, -1, 5, -20], k = 4
return 13

Step 1
从 index = -1 开始, 在index 1 ~ 4 选一个落点 j_1 = 0, 因为1最大

Step 2
从 j_1 = 0 开始, 在 index 2 ~ 5选一个落点 j_2 = 4, 因为7最大

Step 3
从j_2 = 4开始, 在 index 6 ~ 9选一个落点 j_3 = 9

选中arr中1，7，5，-20，最后和为-7

---------------------------------------
假设把上面arr[-2] = -5
最后和为-13，因为倒数第二步跳-1，最后一步跳-20
"""


def maxResult(nums: List[int], k: int) -> int:
    n = len(nums)
    q = deque([])
    q.append(0)  # 这个Q是记录位置的

    sum_dp = [0] * n  # 记录前n个数的最大和
    sum_dp[0] = nums[0]
    print('nums', nums)

    for i in range(1, n):
        # 到当前位置的最大sum
        print('nums[i]', nums[i])
        sum_dp[i] = nums[i] + sum_dp[q[0]]
        # print('dp[i]', sum_dp[i])

        # 窗口往右滑动，每次最多滑一个，所以就一个if就行
        if q[0] < i - k + 1:
            q.popleft()

        print('q2', q)
        # q[-1] 是只保留窗口最大的sum的index

        while q and sum_dp[q[-1]] < sum_dp[i]:
            print('#', sum_dp[q[-1]], sum_dp[i])
            q.pop()
        # 如果pop空了就说明当前位置的最大
        # 到最后会append进队列
        print('q3', q)
        q.append(i)
        print('dp', sum_dp)
        print(q)
        print('-----------------')

    return sum_dp[-1]


def maxResult2(nums: List[int], k: int) -> int:
    sum_dp = [0] * len(nums)
    sum_dp[0] = nums[0]

    q = deque([])
    start_index = 0
    q.append(start_index)

    for i in range(1, len(nums)):
        cur_sum = sum_dp[q[-1]] + nums[i]

        sum_dp[i] = cur_sum
        # 3 4 5

        #     k = 3
        #
        # k - 1 就是自己算上一个位置，然后前面在补2个

        # 如果 i 小于 这个数就是说明不在窗口内了
        if i < i - (k - 1):
            q.popleft()

        while q and cur_sum > sum_dp[q[-1]]:
            q.pop()

        q.append(i)

    return sum_dp[-1]


test_arr = [
    [1, -1, -2, -4, 7, -3, -2, -1, -5, -100],
    [10, -5, -2, 4, 10, 30],
    [1, -5, -20, 4, -1, 3, -6, -3]
]
k_arr = [2, 4, 2]

res_arr = [7, 17, 0]
print(maxResult(test_arr[0], k_arr[1]))

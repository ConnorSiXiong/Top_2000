from typing import List

"""
1. 一开始负数没有考虑
2. 然后这种没有考虑到[0,0,0,0,0] target = 0
"""


def subarraySum(nums: List[int], k: int) -> int:

    count = 0
    start = 0
    round = 0
    while True:
        print('round =', round)
        temp_sum = 0
        for i in range(start, len(nums)):
            print('i =', i)
            cur = nums[i]
            temp_sum += cur
            print("sum =", temp_sum)

            if temp_sum == k:
                count += 1




        # 更新起点
        start += 1
        # 已经到了最后一位, 跳出循环
        round += 1
        if round == len(nums):
            break

    return count
#
#
# a = [-1, -1, 1]
# target = 0

# a = [1,9,1,9,10]
# target = 10

# a = [28,54,7,-70,22,65,-6]
# target = 100



def subarraySum2(nums: List[int], k: int) -> int:
    # [1, 2, 3 ,4 , 5 , 6]
    #
    #  1, 3, 6, 10, 15, 21

    # [1, 1, 1]
    #  1  2  3

    # [-1, -1, 1]
    #  -1, -2, -1

    # [0, 0, 0]
    #  0  0  0

    # [1, 2, -3]
    #  1, 2,  0
    count = 0
    box = {0: 1}
    temp_sum = 0
    for each in nums:
        temp_sum += each
        if temp_sum - k in box.keys():
            count += box.get(temp_sum - k)

        if temp_sum in box.keys():
            box[temp_sum] = box.get(temp_sum) + 1
        else:
            box[temp_sum] = 1

    return count


a = [1,2,1,2]
target = 3

print(subarraySum2(a, target))
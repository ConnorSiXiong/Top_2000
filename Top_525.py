from typing import List

# reference:
# https://www.bilibili.com/video/BV14W411d7SD?from=search&seid=1163975828653429826


def findMaxLength(nums: List[int]) -> int:
    dic = {}
    temp_sum = 0
    result = 0

    for i in range(0, len(nums)):
        current = nums[i]
        if current == 0:
            current = -1
        temp_sum += current

        # 注意
        # 1. 这个等于0等情况
        #    当temp_sum == 0 时候，数组里的0和1的数量正好相等，
        #    所以直接result = i+1 就行了(数组的第一位是0,所以总个数就是index+1)

        # 2. 数组的第一个数为0的情况
        #    [0]
        #    [0, 1, 1]
        if temp_sum == 0:
            result = i + 1
        elif temp_sum in dic:
            previous_i = dic[temp_sum]
            distance = i - previous_i
            result = max(result, distance)
        else:
            dic[temp_sum] = i

    return result


a = [0]


print(findMaxLength(a))
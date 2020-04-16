from typing import List
"""
这个题可以先想到一个遍历解法
即每一次扫到元素i就跳过去
[skip,2,3,4] 左边1    右边2x3x4
[1,skip,3,4] 左边1    右边3x4    
[1,2,skip,4] 左边1x2  右边4 
观察可知，skip位置的结果就是这个数字的 [左边的乘积] 与 [它右边的乘积] 

下面设计的那个算法就是

    在第一个for循环把这个数[左边的乘积]都算出来
    在第二个for循环把这个数[它右边的乘积]与第一轮得到的[左边的乘积]相乘

结果
[24,12,8,6]
"""

def productExceptSelf(nums: List[int]) -> List[int]:
    r = [1] * len(nums)
    print(r)

    anchor = 1
    # left
    for i in range(len(nums)):
        r[i] = anchor
        anchor *= nums[i]

    anchor = 1
    # right
    for i in range(len(nums)-1, -1, -1):
        r[i] *= anchor
        anchor *= nums[i]
    return r



t = [1, 2, 3, 4]
print(productExceptSelf(t))

t = [1, 2, 3, 4]
print("测试一下倒着写for循环")
print("第一种")
# 这一种直接报错了
# 因为 len(t) 在数组的 index 外面
# 而且取不到 0

for i in range(len(t), 0, -1):
    print(i)
print("第二种，正确的一种")
for i in range(len(t) - 1, -1, -1):
    print(i)


# 稍微快一点点
def productExceptSelf2(nums: List[int]) -> List[int]:
    curr = 1
    result = []

    for num in nums:
        result.append(curr)
        curr *= num

    curr = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= curr
        curr *= nums[i]

    return result


def productExceptSelf3(nums: List[int]) -> List[int]:
    result = []
    for i in range (len(nums)):
        temp_product = 1
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                temp_product *= nums[j]
        result.append(temp_product)
    return result


print(productExceptSelf3(t))
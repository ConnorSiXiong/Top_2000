from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    指针指向3个数
    第一个数作为anchor
    """
    n = len(nums)
    if n <= 2:
        return []

    nums.sort()

    if nums[0] > 0:
        return []

    res = []

    for i in range(n - 2):
        # 因为是第一个数作为anchor，所以最后计数的长度-2 ｜ 因为到最后3位数了
        first = nums[i]
        if nums[i] > 1:
            break
        if nums[i] == nums[i - 1] and i > 0:  # 这里要加上i > 0, 不然会失掉[0,0,0]
            continue
        second = i + 1
        third = n - 1

        while second < third:

            sum_of_three = first + nums[second] + nums[third]

            if sum_of_three > 0:
                third -= 1
            elif sum_of_three < 0:
                second += 1
            else:
                res.append([first, nums[second], nums[third]])

                while second + 1 < third and nums[second + 1] == nums[second]:
                    second += 1
                while third - 1 > second and nums[third - 1] == nums[third]:
                    third -= 1

                third -= 1
                second += 1

    return res


a = [-1, 0, 1, 2, -1, -4]

print(threeSum(a))

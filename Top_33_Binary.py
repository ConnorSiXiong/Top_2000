from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        mid_value = nums[mid]
        right_value = nums[right]
        left_value = nums[left]

        if mid_value == target:
            return mid
        if right_value == target:
            return right

        if mid_value > right_value:
            if left_value <= target < mid_value:
                # 这里如果分析 mid的右边，有两种情况，比较绕；所以分析左边
                # 第一种情况 4 5 6 8 1 2   target = 8
                # 另一种情况 4 5 6 0 1 2   target = 1
                right = mid - 1
            else:
                left = mid + 1
        else:
            if right_value >= target > mid_value:
                left = mid + 1
            else:
                right = mid - 1
    return -1


a = [5, 6, 0, 1, 2, 3]
t = 1

b = [1]

print(search(a, 3))


# nums = [4,5,6,7,0,1,2], target = 0
# nums = [4,5,6,7,0,1,2], target = 3

def search2(nums: List[int], target: int) -> int:
    """
    2020.07.09, 18:06
    再做一遍
    看了半天, 没做出来

    2020.07.09 20:00
    再再看一遍

    思路：

    时间复杂度基本就可以提示是用二分查找了，但是关键就在于得到中间的旋转数之后，我们是要搜索左半部分，还是右半部分呢？
    我们来模拟一个例子看下。
    对于数组[0 1 2 4 5 6 7] 共有下列七种旋转方法

    见图片33

    可以看到，加粗的都是升序的，如果中间的数小于最右边的数，则右半段是有序的，
    若中间数大于最右边数，则左半段是有序的，我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定搜索哪边。


    1.先找到哪边是有序的
    2.target在不在有序的一边里面(注意边界)；不在这部分就在另外一边

    3.[left] [mid] [right] 都判断一下算是偷懒，但是有效/ 不增加复杂度
    """
    n = len(nums)

    if n == 0:
        return -1

    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2
        print('mid', mid)
        print('mid value', nums[mid])
        if target == nums[mid]:
            return mid
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right

        if nums[mid] > nums[right]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [4, 5, 6, 7, 8, 9, 2, 3]
target = 3

print(search2(nums, target))

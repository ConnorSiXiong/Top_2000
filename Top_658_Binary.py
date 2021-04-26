from typing import List


#
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         res = []
#         right = self.findTargetIndex(arr, x)
#         left = right - 1
#         for i in range(k):
#             if self.isLeftCloser(arr, left, right, x):
#                 res.append(arr[left])
#                 left -= 1
#             else:
#                 res.append(arr[right])
#                 right += 1
#         return sorted(res)
#
#     def findTargetIndex(self, arr, target):
#         """
#         find the first element in arr >= target
#
#         xxxxxxoooooo
#
#         namely, the first 'o'
#         """
#         left = 0
#         right = len(arr) - 1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             """
#                 这个地方如果写成
#                 if arr[mid] <= target:
#                     left = mid
#                 else:
#                     right = mid
#
#                 在第一个if里，第一个o会被划入xxxxx的一边，
#                 [1，2，5，6，7], target = 4
#                 5也会被划进去
#             """
#             if arr[mid] >= target:
#                 right = mid
#             else:
#                 left = mid
#
#             # if arr[mid] < target:
#             #     left = mid
#             # else:
#             #     right = mid
#
#         if arr[left] >= target:
#             return left
#         if arr[right] >= target:
#             return right
#         return len(arr)
#
#     def isLeftCloser(self, arr, left, right, target):
#         print('left', left)
#         print('right', right)
#         # 自己写的时候没有想清楚边界判断
#         # ------------------------------
#         # 这一种情况是，左边没有（或者是用完了），然后就全部去右边拿
#         if left < 0:
#             return False
#
#         # 这一部分是右边用完了，然后就直接全部去左边拿
#         if right >= len(arr):
#             return True
#         # ------------------------------
#
#         # if abs(arr[left] - target) <= abs(arr[right] - target):
#         # 优化成下面的，可以减少一个abs()函数
#         if target - arr[left] <= arr[right] - target:
#             return True
#         return False
#
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        right = self.findTargetIndex(arr, x)
        left = right - 1
        print('right', right)
        print('left', left)
        for i in range(k):
            if self.isLeftCloser(arr, left, right, x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        return res

    def findTargetIndex(self, arr, target):
        # find index of x >= target

        # 0, 1, 2, 3 , 4 , 5
        #       x

        # 1, 1, 1, 10, 10, 10
        #

        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2

            # ---------  想错了，基础错误  ---------
            # if arr[mid] >= target:
            #     left = mid
            # else:
            #     right = mid
            # ---------  想错了，基础错误  ---------

            if arr[mid] >= target:
                # arr[mid]已经大于等于target
                # 那么target只可能出现在左半部分
                # 等于情况就是正好arr[mid] = target

                # 剩下的从 arr[mid] > target 来看
                # mid 已经大于 target 了，不可能跑到右边更大的部分去找
                # 所以只可能在左边

                # 其实也可以分开写，不容易出错
                # 思维上面就是单独去想一想怎么处理 = 的情况

                right = mid
            else:
                left = mid
        if arr[left] >= target:
            return left
        if arr[right] >= target:
            return right

        return len(arr)

    def isLeftCloser(self, arr, left, right, target):
        # 先判断边界
        if right >= len(arr):
            return True
        if left < 0:
            return False

        if target - arr[left] <= arr[right] - target:
            return True
        return False


a = Solution()
arr = [-2, -1, 1, 2, 3, 4, 5]
arr1 = [1, 1, 1, 10, 10, 10]
print(a.findClosestElements(arr1, 3, 3))

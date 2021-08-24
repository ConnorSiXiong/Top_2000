# from typing import List
#
# arr0 = [-2, -1, 1, 2, 3, 4, 5]
# arr1 = [1, 1, 1, 10, 10, 10]
# arr2 = [-2, -1, 1, 2, 3, 4, 5]
# arr3 = [5, 7, 7, 8, 8, 10]
#
#
# def findClosestElements(arr, target, k):
#     arr = sorted(arr)
#
#     right = findIndex(arr, target)
#     print('right', right)
#     if right < 0:
#         return []
#     left = right - 1
#     res = []
#     for _ in range(k):
#         if checkLeftCloser(arr, left, right, target):
#             res.append(arr[left])
#             left -= 1
#         else:
#             res.append(arr[right])
#             right += 1
#     return sorted(res)
#
#
# def findIndex(arr, target):
#     # OXXXX
#     # get the first X > target
#     left = 0
#     right = len(arr) - 1
#
#     while left + 1 < right:
#         mid = (left + right) // 2
#         if arr[mid] > target:
#             right = mid
#         else:
#             left = mid
#
#     if arr[left] > target:
#         return left
#     if arr[right] > target:
#         return right
#     return -1
#
#
# def checkLeftCloser(arr, left, right, target):
#     if left < 0:
#         return False
#     if right >= len(arr):
#         return True
#     if abs(arr[left] - target) <= abs(arr[right] - target):
#         return True
#     return False
#
#
# # print(findClosestElements(arr3, 9, 3))
#
#
# def minimumAbsDifference(arr):
#     dic = dict()
#     arr = sorted(arr)
#     min_val = float('inf')
#     for i in range(1, len(arr)):
#         key_val = arr[i] - arr[i - 1]
#
#         if key_val < min_val:
#             min_val = key_val
#
#         if key_val not in dic:
#             dic[key_val] = [[arr[i - 1], arr[i]]]
#         else:
#             temp = dic[key_val]
#             temp.append([arr[i - 1], arr[i]])
#             dic[key_val] = temp
#     return dic[min_val]
#
#
# # print(minimumAbsDifference([4, 2, 1, 3]))
#
# arr = [1, 2, 3]
#
#
# # 从arr 里面取k个数，获得他们的全排列
# def test(arr):
#     res = []
#     for i in range(len(arr)):
#         dfs0(arr, i, [], res)
#     return res
#
#
# def dfs0(arr, index, one_set, res):
#     for i in range(len(arr)):
#         if i == index:
#             continue
#         one_set.append(arr[i])
#         dfs0(arr, )
#
#
# grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
#
# import numpy as np
#
#
# def maxAreaOfIsland(grid):
#     max_area = 0
#     grid = np.array(grid)
#     rows = grid.shape[0]
#     cols = grid.shape[1]
#
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i, j] == 0:
#                 continue
#             max_area = max(max_area, dfs(grid, i, j))
#     return max_area
#
#
# def dfs(grid, x, y):
#     if not isValid(grid, x, y):
#         return 0
#     grid[x, y] = 0
#     return 1 + dfs(grid, x + 1, y) + dfs(grid, x - 1, y) + dfs(grid, x, y + 1) + dfs(grid, x, y - 1)
#
#
# def isValid(grid, x, y):
#     if not (0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]):
#         return False
#     if grid[x, y] == 0:
#         return False
#     return True
#
#
# # print(maxAreaOfIsland(grid))
#
# import collections
#
# D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#
#
# def maxAreaOfIsland(grid):
#     max_area = 0
#     q = collections.deque([])
#
#     grid = np.array(grid)
#
#     rows = grid.shape[0]
#     cols = grid.shape[1]
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i, j] == 0:
#                 continue
#             cur_area = 1
#             q.append((i, j))
#             grid[i, j] = 0  # 这个地方写漏了
#
#             while q:
#                 position = q.popleft()
#                 x, y = position[0], position[1]
#
#                 for (dx, dy) in D:
#                     next_x = x + dx
#                     next_y = y + dy
#                     if isValid(grid, next_x, next_y):
#                         cur_area += 1
#                         grid[next_x, next_y] = 0
#                         q.append((next_x, next_y))
#             print(cur_area)
#             max_area = max(max_area, cur_area)
#     return max_area
#
#
# # print(maxAreaOfIsland(grid))
# #
# # def maxAreaOfIsland(grid):
# #     max_area = 0
# #
# #     grid = np.array(grid)
# #     rows = grid.shape[0]
# #     cols = grid.shape[1]
# #     for i in range(rows):
# #         for j in range(cols):
# #             if grid[i, j] == 0:
# #                 continue
# #             max_area = max(dfsM(grid, i, j), max_area)
# #
# #     return max_area
# #
# #
# # def dfsM(grid, x, y):
# #     if not isValid(grid, x, y):
# #         return 0
# #     grid[x][y] = 0
# #     my_area = 1
# #     my_area += dfsM(grid, x + 1, y)
# #     my_area += dfsM(grid, x - 1, y)
# #     my_area += dfsM(grid, x, y + 1)
# #     my_area += dfsM(grid, x, y - 1)
# #     return my_area
# #
# #
# # def isValid(grid, x, y):
# #
# #     if not (0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]):
# #         return False
# #     if grid[x, y] == 0:
# #         return False
# #     return True
# #
# #
# # print(maxAreaOfIsland(grid))
# """
# a = [5, 3, 1, 4, 2]
#
# alice = 2
# a1 = 13
# a = [5, 3, 1, 4]
#
# bob - min
# 1) bob = 5
# sum = 8
#
# 2) bob = 4
# sum = 9
#
#
# b1 = 8
#
# a = [4, 3, 1]
#
# alice = 3
# a1 = 5
#
# a = [4, 3]
# bob = 4
# b1 = 5
#
# print(13+8 - 9 - 5)
# """
#
# import numpy as np
# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         dp = [[0 for _ in range(len(stones))] for _ in range(len(stones))]  # dp table n x n
#         run_sum = [0]  # running sum -> sum [i..j] = run_sum[j] - run_sum[i]
#         s = 0
#
#         ## Calculation of running sum
#         for i in stones:
#             s += i
#             run_sum.append(s)
#         print(run_sum)
#         n = len(stones)
#
#         for k in range(1, n):  # no. of stones left
#             for i in range(0, n - k):  # from each starting point
#                 print('k', k)
#                 print('i', i)
#                 remove_i_stone = (run_sum[i + k + 1] - run_sum[i + 1])  # score after removing i th stone
#                 remove_j_stone = (run_sum[i + k] - run_sum[i])  # score after removing j th stone
#                 print('remove_i_stone', remove_i_stone)
#                 print('remove_j_stone', remove_j_stone)
#                 print('dp')
#                 print(np.array(dp))
#                 if (n - (k + 1)) % 2 == 0:  # alice's move
#                     dp[i][i + k] = max(remove_i_stone + dp[i + 1][i + k],
#                                        remove_j_stone + dp[i][i + k - 1])
#                 else:  # bob's move
#                     dp[i][i + k] = min(-remove_i_stone + dp[i + 1][i + k],
#                                        - remove_j_stone + dp[i][i + k - 1])
#
#         return dp[0][n - 1]
#
#
# a = Solution()
# arr = [5, 3, 1, 4, 2]
# print(a.stoneGameVII(arr))
from collections import Counter
from typing import List

words = [
    ('a', 9),
    ('b', 12),
    ('c', 6),
    ('d', 3),
    ('e', 5),
    ('f', 15)
]


# words = [('e', 9), ('c', 3), ('a', 2), ('b', 2), ('d', 1)]
# words = [('e', 9), ('c', 4), ('a', 2), ('b', 2), ('d', 1)]


# words = [(i[1], i[0]) for i in words]
# print(words)
# print(sorted(words))
#
# words = dict(words)
# words = sorted(words.items(), key=lambda x: x[1])
#
# words = {v: k for k, v in dict(words).items()}
# print(list(words))
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left_weight = '0'
#         self.right_weight = '1'
#         self.left = None
#         self.right = None
#
#
# class HuffmanTree:
#     def __init__(self, words_tuple):
#         self.words_tuple = words_tuple
#         self.words = words_tuple
#         self.words = self.__init_nodes()
#         self.build_tree()
#         self.root = self.words[0][1]
#         self.get_coding_len()
#
#     def __init_nodes(self):
#         arr = []
#         for i in range(len(self.words)):
#             arr.append([self.words[i][1], Node(self.words[i][0])])
#         return sorted(arr, key=lambda i: i[0], reverse=True)
#
#     def build_tree(self):
#         while len(self.words) != 1:
#             self.print_keys()
#             left_set = self.words.pop()
#             right_set = self.words.pop()
#             left_node = left_set[1]
#             right_node = right_set[1]
#             new_node = Node(left_set[0] + right_set[0])
#             new_node.left = left_node
#             new_node.right = right_node
#             self.words.append([new_node.value, new_node])
#             self.__sort_words()
#
#     def __sort_words(self):
#         self.words = sorted(self.words, key=lambda i: i[0], reverse=True)
#
#     def print_keys(self):
#         arr = []
#         for i in self.words:
#             arr.append(i[0])
#         print(arr)
#
#     def coding_tree(self):
#         res = []
#         path = []
#         self._dfs(self.root, path, res)
#         return res
#
#     def _dfs(self, node, path, res):
#         if str.isalpha(str(node.value)):
#             res.append([node.value, ''.join(path[:])])
#             return
#
#         if node.right:
#             path.append(node.right_weight)
#             self._dfs(node.right, path, res)
#             path.pop()
#         if node.left:
#             path.append(node.left_weight)
#             self._dfs(node.left, path, res)
#             path.pop()
#
#     def get_coding_len(self):
#         frequency = dict(self.words_tuple)
#         coding_res = dict(self.coding_tree())
#         # # debug用
#         # print(frequency)
#         # print(coding_res)
#         return sum(len(coding_res[i]) * frequency[i[0]] for i in coding_res.keys())
#
#
# class BinaryTree:
#     def __init__(self, words_tuple):
#         self.words_tuple = words_tuple
#         self.root = self.build_tree()
#
#     def build_tree(self):
#         notes = self.get_all_words()
#         root = Node(0)
#         cur_node = root
#
#         while notes:
#             left_node = notes.pop()
#             cur_node.left = Node(left_node)
#             if len(notes) == 1:
#                 cur_node.right = Node(notes.pop())
#             else:
#                 cur_node.right = Node(0)
#             cur_node = cur_node.right
#         return root
#
#     def get_all_words(self):
#         return [i[0] for i in self.words_tuple]
#
#     def coding_tree(self):
#         res = []
#         path = []
#         self._dfs(self.root, path, res)
#         return res
#
#     def _dfs(self, node, path, res):
#         if str.isalpha(str(node.value)):
#             res.append([node.value, ''.join(path[:])])
#             return
#
#         if node.right:
#             path.append(node.right_weight)
#             self._dfs(node.right, path, res)
#             path.pop()
#         if node.left:
#             path.append(node.left_weight)
#             self._dfs(node.left, path, res)
#             path.pop()
#
#     def get_coding_len(self):
#         frequency = dict(self.words_tuple)
#         coding_res = dict(self.coding_tree())
#         # # debug用
#         # print(frequency)
#         # print(coding_res)
#         return sum(len(coding_res[i]) * frequency[i[0]] for i in coding_res.keys())
#
#
# b = BinaryTree(words)
# print(b.get_coding_len())
#
# a = []
#
# a.append([1, 'haha'])
# a.append([1000, 'bb'])
# a.append([3, 'cc'])
#
# t = HuffmanTree(words)
#
#
#
# from collections import deque
#
# prerequisites = [
#     [2, 1],
#     [2, 0],
#     [3, 2]
# ]
#
# from collections import defaultdict
#
#
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         edges = defaultdict(list)
#         indge = [0] * numCourses
#         res = 0
#
#         for i in prerequisites:
#             edges[i[1]].append(i[0])
#             indge[i[0]] += 1
#
#         q = deque([u for u in range(numCourses) if indge[u] == 0])
#
#         while q:
#             u = q.popleft()
#             res += 1
#             for v in edges[u]:
#                 indge[v] -= 1
#                 if indge[v] == 0:
#                     q.append(v)
#         return res == numCourses
#
#
# a = Solution()
#
# a.canFinish(4, prerequisites)
#
# """
# >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> d.default_factory
# <type 'list'>
# >>> for k, v in s:
# ...     d[k].append(v)
# >>> d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# >>> d
# defaultdict(<type 'list'>, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})
# """
#
# prerequisites = [
#     [2, 1],
#     [2, 0],
#     [3, 2]
# ]
#
# a = Solution()
#
# print(a.canFinish(4, prerequisites))
# class Solution2:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         pre_course_dict = defaultdict(list)
#         course_prerequisites = [0] * numCourses
#
#         for i in prerequisites:
#             pre_course_dict[i[1]].append(i[0])
#             course_prerequisites[i[0]] += 1
#
#         q = deque([i for i in range(numCourses) if course_prerequisites[i] == 0])
#         res = 0
#         while q:
#             finished = q.popleft()
#             res += 1
#             for i in pre_course_dict[finished]:
#                 course_prerequisites[i] -= 1
#                 if course_prerequisites[i] == 0:
#                     q.append(i)
#         return res == numCourses
#
#
# b = Solution2()
#
# print(b.canFinish(4, prerequisites))
#
# prerequisites = [
#     [2, 1],
#     [2, 0],
#     [3, 2]
# ]
#
#
# class Solution3:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         class_dict = defaultdict(list)
#         lesson_arr = [0] * numCourses
#
#         for i in prerequisites:
#             lesson_arr[i[0]] += 1
#             class_dict[i[1]].append(i[0])  # 课程加一个前置
#
#         q = deque([i for i in range(numCourses) if lesson_arr[i] == 0])  # -> 队列初始化
#
#         while q:
#             cur = q.popleft()
#
#             for i in class_dict[cur]:
#                 lesson_arr[i] -= 1
#                 if lesson_arr[i] == 0:
#                     q.append(i)
#
#         return sum(lesson_arr) == 0
#
#
#
#
#
#
# a = Solution3()
# print(a.canFinish(4, prerequisites))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
level_1_left = TreeNode(1)
level_1_right = TreeNode(4)

level_2_left_left = TreeNode(3)
level_2_right_left = TreeNode(1)
level_2_right_right = TreeNode(5)

root.left = level_1_left
root.right = level_1_right

level_1_left.left = level_2_left_left
level_1_right.left = level_2_right_left
level_1_right.right = level_2_right_right

"""
               3 
               
        1             4
        
   3               1       5

"""

#
# class Solution:
#     def findGCD(self,  nums: List[int]) -> int:
#         nums = sorted(nums)
#         a = nums[0]
#         b = nums[-1]
#         return self.hcf(a, b)
#
#     def hcf(self, a, b):
#         c, d = max(a, b), min(a, b)
#         e = 1
#         while e != 0:
#             e = c % d
#             c, d = d, e
#         return c
#
#
#
# a= Solution()
#
# print(a.findGCD([2,5,6,9,10]))

# 有n个长度为n的二进制01
#
# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n = len(nums)
#
#         start_index = 0
#         change_index = start_index
#         temp = ["1"] * n
#         while 1:
#             if ''.join(temp) not in nums:
#                 return ''.join(temp)
#             temp[change_index] = '0'
#
#             change_index += 1
#             if change_index == n+1:
#                 start_index += 1
#                 change_index = start_index
#
#
#
#
#     def dfs(self, n, index, comb, box):
#         if len(comb) == n:
#             box.append(''.join(comb[:]))
#             return
#         for i in range(index, n):
#             comb.append('1')
#             self.dfs(n, i+1, comb[:], box)
#             comb.pop()
#             comb.append('0')
#             self.dfs(n, i+1, comb, box)
#
# # 最多只有16种组合
# # 我只用找到其中某一位置都没出现的都行
#
# a = Solution()
#
# print(a.findDifferentBinaryString(['111','110','000']))
#
# # print(set(sorted(["111","011","001"])))
#
# """
# "00001101111011","11011001010101","00001000000001","00011100000000","01101111001010","01011011010101","00110100111111","10001100101110","01000000010011","00110000101011","01101010000101","10000111010100","11000000111000","00101101110110"]
# """

import numpy as np

mat = [[3, 2, 1], [40, 5, 6], [7, 8, 9]]


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        for row in mat:
            row = sorted(row)

        return 0


# a = Solution()
# a.minimizeTheDifference(mat, 10)



class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        box = Counter(set(nums))
        cur = ''
        res = ''
        flag = True

        def dfs(cur_str, box, index, n):
            print('comb', cur_str)
            nonlocal flag
            nonlocal res
            if not flag:
                return

            if index == n:
                if box[cur_str] == 0:
                    res = cur_str
                    flag = False
                return

            for i in range(2):
                cur_str += str(i)
                dfs(cur_str, box, index + 1, n)
                cur_str = cur_str[:-1]

        dfs(cur, box, 0, len(nums))
        print(res)
        return res


class Solution3:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        stop = False
        n = len(nums)
        box = Counter(set(nums))

        def dfs(comb, box, n):
            print('comb', comb)
            nonlocal res
            nonlocal stop
            if stop is True:
                return

            if len(comb) == n:
                if box[comb] == 0:
                    res = comb
                    stop = True
                    return
                return

            for i in range(2):
                comb += str(i)
                dfs(comb, box, n)
                comb = comb[:-1]

        dfs('', box, n)
        print(res)
        return res



a = Solution3()
# a.findDifferentBinaryString(["00001101111011","11011001010101","00001000000001","00011100000000","01101111001010","01011011010101","00110100111111","10001100101110","01000000010011","00110000101011","01101010000101","10000111010100","11000000111000","00101101110110"])
a.findDifferentBinaryString(['000','001','011'])
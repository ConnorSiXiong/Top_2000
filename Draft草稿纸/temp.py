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


class Node:
    def __init__(self, value):
        self.value = value
        self.left_weight = '0'
        self.right_weight = '1'
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self, words_tuple):
        self.words_tuple = words_tuple
        self.words = words_tuple
        self.words = self.__init_nodes()
        self.build_tree()
        self.root = self.words[0][1]
        self.get_coding_len()

    def __init_nodes(self):
        arr = []
        for i in range(len(self.words)):
            arr.append([self.words[i][1], Node(self.words[i][0])])
        return sorted(arr, key=lambda i: i[0], reverse=True)

    def build_tree(self):
        while len(self.words) != 1:
            self.print_keys()
            left_set = self.words.pop()
            right_set = self.words.pop()
            left_node = left_set[1]
            right_node = right_set[1]
            new_node = Node(left_set[0] + right_set[0])
            new_node.left = left_node
            new_node.right = right_node
            self.words.append([new_node.value, new_node])
            self.__sort_words()

    def __sort_words(self):
        self.words = sorted(self.words, key=lambda i: i[0], reverse=True)

    def print_keys(self):
        arr = []
        for i in self.words:
            arr.append(i[0])
        print(arr)

    def coding_tree(self):
        res = []
        path = []
        self._dfs(self.root, path, res)
        return res

    def _dfs(self, node, path, res):
        if str.isalpha(str(node.value)):
            res.append([node.value, ''.join(path[:])])
            return

        if node.right:
            path.append(node.right_weight)
            self._dfs(node.right, path, res)
            path.pop()
        if node.left:
            path.append(node.left_weight)
            self._dfs(node.left, path, res)
            path.pop()

    def get_coding_len(self):
        frequency = dict(self.words_tuple)
        coding_res = dict(self.coding_tree())
        # # debug用
        # print(frequency)
        # print(coding_res)
        return sum(len(coding_res[i]) * frequency[i[0]] for i in coding_res.keys())


class BinaryTree:
    def __init__(self, words_tuple):
        self.words_tuple = words_tuple
        self.root = self.build_tree()

    def build_tree(self):
        notes = self.get_all_words()
        root = Node(0)
        cur_node = root

        while notes:
            left_node = notes.pop()
            cur_node.left = Node(left_node)
            if len(notes) == 1:
                cur_node.right = Node(notes.pop())
            else:
                cur_node.right = Node(0)
            cur_node = cur_node.right
        return root

    def get_all_words(self):
        return [i[0] for i in self.words_tuple]

    def coding_tree(self):
        res = []
        path = []
        self._dfs(self.root, path, res)
        return res

    def _dfs(self, node, path, res):
        if str.isalpha(str(node.value)):
            res.append([node.value, ''.join(path[:])])
            return

        if node.right:
            path.append(node.right_weight)
            self._dfs(node.right, path, res)
            path.pop()
        if node.left:
            path.append(node.left_weight)
            self._dfs(node.left, path, res)
            path.pop()

    def get_coding_len(self):
        frequency = dict(self.words_tuple)
        coding_res = dict(self.coding_tree())
        # # debug用
        # print(frequency)
        # print(coding_res)
        return sum(len(coding_res[i]) * frequency[i[0]] for i in coding_res.keys())


b = BinaryTree(words)
print(b.get_coding_len())

a = []

a.append([1, 'haha'])
a.append([1000, 'bb'])
a.append([3, 'cc'])

t = HuffmanTree(words)

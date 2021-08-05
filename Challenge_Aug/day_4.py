"""
day 4
leetcode 113 没做过

看了一下，用dfs backtracking

Author: Alex
Date: 05/08/2021 - NZ Auckland
      14:40 pm - 14:59 pm
      这个题目一定是要求路径得走到叶子节点，没有考虑到这个点

      15:04 pm - 15:05 pm
      被一个奇怪的test case卡住了

      15:05 pm - 15:16 pm
      发现回溯的时候，更新pre_sum写漏了


"""

from typing import List
from time import sleep

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

level_0 = TreeNode(5)
level_1_left = TreeNode(4)
level_1_right = TreeNode(8)

level_2_left_left = TreeNode(7)
level_2_right_left = TreeNode(13)
level_2_right_right = TreeNode(3)

level_0.left = level_1_left
level_0.right = level_1_right

level_1_left.left = level_2_left_left
level_1_right.left = level_2_right_left
level_1_right.right = level_2_right_right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.dfs(root, [], 0, res, target)
        return res

    def dfs(self, node, comb, pre_sum, res, target):
        comb.append(node.val)
        pre_sum += node.val
        if pre_sum == target and node.left is None and node.right is None:
            res.append(comb[:])

        if node.left:
            self.dfs(node.left, comb, pre_sum, res, target)
        if node.right:
            self.dfs(node.right, comb, pre_sum, res, target)
        pre_sum -= node.val  # 这一句话漏了，test case 114 没有通过
        comb.pop()

a = Solution()

print(a.pathSum(level_0, 16))


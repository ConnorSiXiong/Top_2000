from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root, index):
            arr_val = arr[index]

            if root is None or root.val != arr_val:
                return False

            if index == len(arr) - 1:
                return not root.left and not root.right
            return dfs(root.left, index + 1) or dfs(root.right, index + 1)

        return dfs(root, 0)


# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
"""
复习
怎么把树的branch切断构成两个树

Author: Alex
Date: 30/08/2021 - NZ Auckland
      10:37 - 10:50 - 没做出来

      思路：
      1。使用inorder traverse, 累加所有的nodes
      2。存到数组里，数组的最后一个就是整个树的sum，然后用树的sum减去每一个node打擂台

      10:50 - 11:02
      看了下怎么求子树的和, 写出来了 （其实是不熟悉后序遍历）

      11:02 - 11:09
      一个优化，用 () 速度比 [] 快, 最后return的一行代码的遍历



"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left1 = TreeNode(4)
left2 = TreeNode(5)
right1 = TreeNode(6)

root.left = left
root.right = right
left.left = left1
left.right = left2
right.right = right1


class Solution:
    def maxProduct(self, root) -> int:
        if not root:
            return None
        box = []
        self.dfs(root, box)
        tree_sum = max(box)
        return max((i * (tree_sum - i) for i in box)) % (10 ** 9 + 7)

    def dfs(self, node, box):
        if not node:
            return 0
        left_sum = self.dfs(node.left, box)
        right_sum = self.dfs(node.right, box)
        cur_sum = left_sum + right_sum + node.val
        box.append(cur_sum)
        return cur_sum


a = Solution()
print(a.maxProduct(root))

"""
day 19

leetcode 1339 没做过
一开始没想出来思路


看了别人的解法，
核心是 res = left * (sum - right)
因为每次只用把整个树分成两个子树就行了

思路1：
traverse统计每一个子树的和, 然后枚举比较
先用这个思路做一下试试，枚举的那一步还能继续优化

思路2:
求和部分用bfs来做一遍

Author: Alex
Date:
20/08/2021 - NZ Auckland
12:10 pm - 12:08 pm, 按照上面的思路1做出来了

12:10 pm -

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
level_1_left = TreeNode(1)
level_1_right = TreeNode(4)

level_2_left_left = TreeNode(30)
level_2_right_left = TreeNode(1)
level_2_right_right = TreeNode(5)

root.left = level_1_left
root.right = level_1_right

level_1_left.left = level_2_left_left
level_1_right.left = level_2_right_left
level_1_right.right = level_2_right_right

"""
         3
     
     1        4
     
 30          1     5

"""

from collections import deque


class Solution:
    def maxProduct(self, root) -> int:
        if not root:
            return 0
        box = []
        self.dfs(root, box)
        tree_sum = box.pop()
        return max(i * (tree_sum - i) for i in box) % (10 ** 9 + 7)

    def dfs(self, node, box):
        if node is None:
            return 0
        cur_sum = self.dfs(node.left, box) + self.dfs(node.right, box) + node.val
        box.append(cur_sum)
        return cur_sum


a = Solution()
print(a.maxProduct(root))


class Solution2:
    def maxProduct(self, root) -> int:
        if not root:
            return 0
        tree_sum = self.bfs(root)
        res_candidate = [0]
        self.dfs(root, res_candidate, tree_sum)
        print(res_candidate[0])
        return res_candidate[0] % (10 ** 9 + 7)


    def bfs(self, root_node):
        q = deque([])
        q.append(root_node)
        tree_sum = 0
        while q:
            cur = q.popleft()
            tree_sum += cur.val
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return tree_sum

    def dfs(self, node, res_candidate, tree_sum):
        if node is None:
            return 0
        left = self.dfs(node.left, res_candidate, tree_sum)
        right = self.dfs(node.right, res_candidate, tree_sum)

        res_candidate[0] = max(res_candidate[0], left * (tree_sum - left), right * (tree_sum - right))
        return left + right + node.val


a = Solution2()
a.maxProduct(root)

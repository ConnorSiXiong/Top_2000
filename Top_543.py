class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    def tree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, result: list) -> int:
            if node is None:
                return 0
            left = dfs(node.left, result)
            right = dfs(node.right, result)
            result[0] = max(result[0], left + right)
            return max(left, right) + 1

        result = [0]
        dfs(root, result)
        return result[0]


a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)
a.right = TreeNode(5)

b = Solution
print(b.tree(b, a))
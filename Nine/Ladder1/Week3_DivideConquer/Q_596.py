class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

root = TreeNode(1)

l = TreeNode(2)

root.left = l

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.min_val = float('inf')
        self.res = None
        self.getSubSum(root)
        print(self.res.val)
        return self.res

    def getSubSum(self, node):
        if node is None:
            return 0

        left_sum = self.getSubSum(node.left)
        right_sum = self.getSubSum(node.right)
        cur_sum = left_sum + right_sum + node.val

        if cur_sum < self.min_val:
            self.min_val = cur_sum
            self.res = node
        return cur_sum

a = Solution()
a.findSubtree(root)
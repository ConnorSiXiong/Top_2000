from typing import List

"""
做这个题时发现对数组切片操作不熟悉
记录一下

arr = [5,7,1]

1） 
arr[1:2] => 7
 
2）
arr[1:1] => None

3）
arr[start: end]
- 切片含头不含尾

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.splitTree(preorder, inorder)

    def splitTree(self, preorder, inorder):
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        if not preorder or not inorder:
            return None

        pop_val = preorder[0]
        cur_node = TreeNode(pop_val)

        split_index = inorder.index(pop_val)

        left_preorder = preorder[1:split_index + 1]
        right_preorder = preorder[split_index + 1:]
        left_inorder = inorder[:split_index]
        right_inorder = inorder[split_index + 1:]

        cur_node.left = self.splitTree(left_preorder, left_inorder)
        cur_node.right = self.splitTree(right_preorder, right_inorder)
        return cur_node


a = [1, 2, 4, 5, 8, 9, 3, 6, 10, 7]
b = [4, 2, 8, 5, 9, 1, 6, 10, 3, 7]

print(a[1:1])

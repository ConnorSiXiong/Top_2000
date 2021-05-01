from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    res, q =[], [root]
    while q:
        val, tmp = [], []
        for node in q:
            val.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

        res.append(val)
        q = tmp

    return res[::-1]
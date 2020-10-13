class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)

    else:
        root.left = self.insertIntoBST(root.left, val)

    return root
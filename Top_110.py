class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


l1 = TreeNode(1)
l2_l = TreeNode(2)
l2_r = TreeNode(3)
l3_ll = TreeNode(4)
l3_lr = TreeNode(5)
l3_rr = TreeNode(6)
l4_rrl = TreeNode(7)
l4_rrr = TreeNode(8)
l5_rrrr = TreeNode(9)
l6_rrrrr = TreeNode(10)

l1.left = l2_l
l1.right = l2_r

l2_l.left = l3_ll
l2_l.right = l3_lr

l2_r.right = l3_rr

l3_rr.left = l4_rrl
l3_rr.right = l4_rrr
l4_rrr.right = l5_rrrr
l5_rrrr.right = l6_rrrrr


def isBalanced(root: TreeNode) -> bool:
    if not root:
        return True
    res, _ = getHeight(root)
    return res


def getHeight(node):
    # 走完了
    if not node:
        return True, 0

    left_balance, left_height = getHeight(node.left)
    right_balance, right_height = getHeight(node.right)

    height = max(left_height, right_height) + 1

    if not left_balance or not right_balance:
        return False, height
    if abs(left_height - right_height) > 1:
        return False, height

    return True, height


# this solution uses global variable
# so mark it here
def isBalanced2(root: TreeNode) -> bool:
    balanced = True

    def getdepth(node=root):
        nonlocal balanced
        if not node:
            return 0
        left_depth = getdepth(node.left)
        right_depth = getdepth(node.right)
        if abs(left_depth - right_depth) > 1:
            balanced = False
        return max(left_depth, right_depth) + 1

    getdepth()
    return balanced


print(isBalanced2(l1))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

root = TreeNode(5)
l1_left = TreeNode(4)
l1_right = TreeNode(9)

l2_left_left = TreeNode(2)
l2_right_left = TreeNode(8)
l2_right_right = TreeNode(10)

root.left = l1_left
root.right = l1_right

l1_left.left = l2_left_left

l1_right.left = l2_right_left
l1_right.right = l2_right_right


def closestValue(root, target):
    return 0

def compare(node, target):
    """

    {10,5,15,3,6,12,18,#,4,#,8}
    target = 4.12
    正确：4
    实际返回：5
    """
    diff = abs(target - node.val)
    diff2 = float('inf')
    diff3 = float('inf')
    if target > node.val and node.right:
        diff2 = abs(target - node.right.val)
    if target < node.val and node.left:
        diff3 = abs(target - node.left.val)
    if diff == min(diff, diff2, diff3):
        return node.val
    else:
        if target > node.val:
            return compare(node.right, target)
        else:
            return compare(node.left, target)

print(compare(root, 11))
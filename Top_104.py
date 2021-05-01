def maxDepth(root) -> int:
    return check_depth(root)

def check_depth(node):
    if not node:
        return 0

    left_height = check_depth(node.left)
    right_height = check_depth(node.right)

    height = max(left_height, right_height) + 1
    return height

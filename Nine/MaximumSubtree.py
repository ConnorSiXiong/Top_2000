class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


l1 = TreeNode(1)
l2_l = TreeNode(-5)
l2_r = TreeNode(2)
l3_ll = TreeNode(0)
l3_lr = TreeNode(3)
l3_rl = TreeNode(-4)
l3_rr = TreeNode(-5)

l1.left = l2_l
l1.right = l2_r

l2_l.left = l3_ll
l2_l.right = l3_lr

l2_r.left = l3_rl
l2_r.right = l3_rr


def findSubtree(root):
    # write your code here
    if not root:
        return None

    max_val = float('-inf')
    res = root

    def getSubtreeSum(node):

        nonlocal max_val
        nonlocal res
        if not node:
            return 0
        left_sum = getSubtreeSum(node.left)
        right_sum = getSubtreeSum(node.right)
        cur_sum = left_sum + right_sum + node.val
        if cur_sum > max_val:
            max_val = cur_sum  # 写的时候忘了更新
            res = node
        return cur_sum

    getSubtreeSum(root)
    print(res.val)
    return res


print(findSubtree(l1))

# 思考:
# 这个题怎么写成递归函数两个返回值的写法？

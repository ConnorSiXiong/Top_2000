import sys


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


findSubtree(l1)


# 思考:
# 这个题怎么写成递归函数两个返回值的写法？
# 第二天，解决了这个问题, 就是要把那个值给返回回去


def findSubtree2(root):
    max_val, node, max_sum = getSumSubtree(root)
    print(node.val)
    return node


def getSumSubtree(node):
    # 叶子结点的下一层
    if not node:
        return -sys.maxsize, node, 0

    left_max, left_node, left_sum = getSumSubtree(node.left)
    right_max, right_node, right_sum = getSumSubtree(node.right)

    cur_sum = left_sum + right_sum + node.val

    if left_max == max(left_max, right_max, cur_sum):
        return left_max, left_node, cur_sum
    if right_max == max(right_max, left_max, cur_sum):
        return right_max, right_node, cur_sum
    return cur_sum, node, cur_sum


findSubtree2(l1)


# ------------- 草稿 -----------------
# -------- 草稿的有更多打印信息 ---------

def findMaxSumSubtree(root):
    i = 0
    max_val, root_node, sum_of_tree = getSubtreeSum(root, i)
    return max_val, root_node.val, sum_of_tree


def getSubtreeSum(node, i):
    if not node:
        return -sys.maxsize, node, 0
    i += 1
    left_max, left_node, left_sum = getSubtreeSum(node.left, i)
    right_max, right_node, right_sum = getSubtreeSum(node.right, i)

    print('Tree Depth:', i)
    print('left_sum', left_sum)
    print('right_sum', right_sum)
    cur_sum = left_sum + right_sum + node.val
    print('node.val', node.val)
    print('cur_sum', cur_sum)
    print('----------')
    if left_max == max(left_max, right_max, cur_sum):
        return left_max, left_node, cur_sum
    if right_max == max(left_max, right_max, cur_sum):
        return right_max, right_node, cur_sum
    return cur_sum, node, cur_sum


print(findMaxSumSubtree(l1))

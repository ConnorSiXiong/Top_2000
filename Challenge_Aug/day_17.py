"""
day 17

leetcode 1448 没做过

题目是要统计 子节点.value >= 所有父节点.value 的 nodes

数量级:
The number of nodes in the binary tree is in the range [1, 10^5].

Each node's value is between [-10^4, 10^4].

要想办法剪枝 - 因为10^5

dfs, backtracking


----- 想清楚再下笔 -----


Author: Alex
Date: 18/08/2021 - NZ Auckland
      15:25 pm - 15:48 pm
      思路错了，backtrack的时候不需要pop，直接往下就行了

      15:48 - 16:15
      调整了添加当前元素进入path的位置
      添加了初始的极小值
      但是有一个用例测试通不过

      16:20 - 16:27
      换了一个思路，不用考虑过去的值，直接往前计算

      16:30 - 16:50
      work out solution 1
      解法最后少了一个pop

      那么：backtracking 的 pop什么时候用？
"""


def generate_tree(vals):
    if len(vals) == 0:
        return None
    que = []  # 定义队列
    fill_left = True  # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    for val in vals:
        node = TreeNode(val) if val else None  # 非空值返回节点类，否则返回 None
        if len(que) == 0:
            root = node  # 队列为空的话，用 root 记录根结点，用来返回
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False  # 填充过左儿子后，改变记号状态
            if node:  # 非 None 值才进入队列
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0)  # 填充完右儿子，弹出节点
            fill_left = True  #
    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(3)
# level_1_left = TreeNode(1)
# level_1_right = TreeNode(4)
#
# level_2_left_left = TreeNode(3)
# level_2_right_left = TreeNode(1)
# level_2_right_right = TreeNode(5)
#
# root.left = level_1_left
# root.right = level_1_right
#
# level_1_left.left = level_2_left_left
# level_1_right.left = level_2_right_left
# level_1_right.right = level_2_right_right
#



root = TreeNode(-1)
level_1_left = TreeNode(5)
level_1_right = TreeNode(-2)


level_2_right_left = TreeNode(2)
level_2_right_right = TreeNode(-2)
root.left = level_1_left
root.right = level_1_right
level_1_right.left = level_2_right_left
level_1_right.right = level_2_right_right

level_2_left_left = TreeNode(4)
level_2_left_right = TreeNode(4)

level_1_left.left = level_2_left_left
level_1_left.right = level_2_left_right

level_3 = TreeNode(-4)
level_4 = TreeNode(0)
level_5 = TreeNode(3)

level_2_left_right.left = level_3
level_3.left = level_4
level_4.left = level_5

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, [float('-inf')], res)
        return len(res)

    def dfs(self, node, path, res):

        if node is None:
            return

        if node.val >= sorted(path)[-1]:
            res.append(1)
        path.append(node.val)

        if node.left:
            self.dfs(node.left, path, res)
            path.pop()
        if node.right:
            self.dfs(node.right, path, res)
            path.pop()


class Solution2(object):
    def goodNodes(self, root):
        self.res = 0

        def dfs(node, maximum):
            if not node:
                return
            if node.val >= maximum:
                self.res += 1
                maximum = max(node.val, maximum)

            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, root.val)
        return self.res


a = Solution()
print(a.goodNodes(root))


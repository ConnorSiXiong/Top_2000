import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> List[List[int]]:
    # ----- 这个写掉了 ------
    if not root:
        return []
    # ----- 这个写掉了 ------

    queue = collections.deque([root])
    res = []

    while queue:
        res.append([i.val for i in queue])
        cur_nodes_num = len(queue)

        for i in range(cur_nodes_num):

            cur_node = queue.popleft()
            left_child = cur_node.left
            right_child = cur_node.right

            if left_child is not None:
                queue.append(left_child)
            if right_child is not None:
                queue.append(right_child)
    return res


l1 = TreeNode(1)
l2_l = TreeNode(2)
l2_r = TreeNode(3)
l3_ll = TreeNode(4)
l3_lr = TreeNode(5)
l3_rr = TreeNode(6)
l4_rrl = TreeNode(7)
l4_rrr = TreeNode(8)

l1.left = l2_l
l1.right = l2_r

l2_l.left = l3_ll
l2_l.right = l3_lr

l2_r.right = l3_rr

l3_rr.left = l4_rrl
l3_rr.right = l4_rrr

print(levelOrder(l1) == [[1], [2, 3], [4, 5, 6], [7, 8]])

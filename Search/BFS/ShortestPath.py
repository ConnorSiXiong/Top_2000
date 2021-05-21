import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


l0 = TreeNode(1)

l1_l = TreeNode(2)
l1_r = TreeNode(3)

l2_ll = TreeNode(4)
l2_lr = TreeNode(5)

l3_lll = TreeNode(6)

l0.left = l1_l
l0.right = l1_r

l1_l.left = l2_ll
l1_l.right = l2_lr

l2_ll.left = l3_lll


def getShortestPath(root):
    paths = []
    if not root:
        return paths

    node_q = collections.deque([root])
    path_q = collections.deque([str(root.val)])

    while node_q:
        q_size = len(node_q)

        for _ in range(q_size):
            cur_node = node_q.popleft()
            path = path_q.popleft()

            if cur_node.left is None and cur_node.right is None:
                paths.append(path)
                print(paths)
                return

            if cur_node.left:
                node_q.append(cur_node.left)
                path_q.append(path + '->' + str(cur_node.left.val))
            if cur_node.right:
                node_q.append(cur_node.right)
                path_q.append(path + '->' + str(cur_node.right.val))
    return paths


getShortestPath(l0)

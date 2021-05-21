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

l0.left = l1_l
l0.right = l1_r

l1_l.left = l2_ll
l1_l.right = l2_lr


def getShortestPath(root):
    if not root:
        return None

    q = collections.deque([])
    q.append(root)

    paths = {}
    if root.left:
        paths[root.left.val] = [root.val]
    if root.right:
        paths[root.right.val] = [root.val]

    while q:
        q_size = len(q)
        print(paths)
        print('----------------')
        print('queue')
        for i in q:
            print(i.val)
        print('----------------')

        for _ in range(q_size):
            cur_node = q.popleft()
            if cur_node.left is None and cur_node.right is None:
                print(paths[cur_node.val].append(cur_node.val))
                return paths[cur_node.val].append(cur_node.val)

            if cur_node.left:
                paths[cur_node.left.val].append(cur_node.val)
                print(cur_node.val)
                print(paths[cur_node.val])
                paths[cur_node.left.val] = paths[cur_node.val]
                q.append(cur_node.left)
            if cur_node.right:
                paths[cur_node.right.val].append(cur_node.val)
                paths[cur_node.right.val] = paths[cur_node.val]
                q.append(cur_node.right)
            print(paths)
            del paths[cur_node.val]

    return None


getShortestPath(l0)
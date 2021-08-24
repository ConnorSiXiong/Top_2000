"""
day 23
LeeCode


思路:
10^4 个 nodes

traverse the tree and store all the visited val in a dict

---> then the exercise becomes to find [two sum]


Author: Alex
Date:
17:23 - 17:40
完成基本结构

17:40 - 17:50
Failed Cases:
1) [1] , 2
2) [2, 1, -3], 2
3) [2, 1, null, 0], 2

其实用set就行了，自己写复杂了，弄了个字典处理，而且还出错了...




"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
left1 = TreeNode(1)
right1 = TreeNode(5)
left2 = TreeNode(-4)
right3 = TreeNode(0)

root.left = left1
root.right = right1

left1.left = left2
left2.right = right3
k = 2


class Solution:
    """
    这个BST无法通过网站

                2

            1       5

        -4

            0
    """

    def findTarget(self, root, k: int):
        # if k == root.val:
        #     return False

        # 这一种情况不能算，因为当出现[2,-1,3]的BST，target = 2的时候，这个算法就报错了

        if root.left is None and root.right is None:
            return False

        q = deque([])
        q.append(root)
        nodes_dict = {}

        while q:
            cur_node = q.popleft()

            if self.checkExist(nodes_dict, cur_node.val, k):
                return True

            nodes_dict[cur_node.val] = 1
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

        return False

    def checkExist(self, node_dict, cur_val, target):
        return True if (target - cur_val) in node_dict else False


class Solution2:
    def findTarget(self, root, k: int):
        # if k == root.val:
        #     return False

        # 这一种情况不能算，因为当出现[2,-1,3]的BST，target = 2的时候，这个算法就报错了
        if not root:
            return False

        if root.left is None and root.right is None:
            return False

        q = deque([])
        q.append(root)
        nodes_set = set()

        while q:
            cur_node = q.popleft()
            if k - cur_node.val in nodes_set:
                return True
            nodes_set.add(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return False


a = Solution()
print(a.findTarget(root, 2))
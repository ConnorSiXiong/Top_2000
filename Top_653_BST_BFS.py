"""
复习
在树中找到两个node，相加可以得到target

Author: Alex
Date: 30/08/2021 - NZ Auckland
      10:00 - 10：10

      思路：
      BFS：队列+set
"""
from collections import deque
class Solution:
    def findTarget(self, root, k: int) -> bool:
        if not root:
            return False
        q = deque([])
        q.append(root)

        node_set = set()

        while q:
            cur_node = q.popleft()
            # 下面那种写法避免了考虑set里只有一个数的情况
            if k - cur_node.val in node_set:
                return True
            node_set.add(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return False

from typing import List

from TreeNode import TreeNode


def bstFromPreorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    stack = [root]
    for value in preorder[1:]:
        if value < stack[-1].val:
            stack[-1].left = TreeNode(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = TreeNode(value)
            stack.append(last.right)
    return root


a = [8,5,1,7,10,12]

# print(bstFromPreorder(a).right.left)

stack = [1]

stack.append(5)

stack.append(10)

print(stack.pop())
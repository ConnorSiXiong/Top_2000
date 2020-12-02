import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.L = head


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        arr = []
        L = self.L
        while True:
            cur_val = L.val

            arr.append(cur_val)
            if L.next:
                L = L.next
            else:
                break
        return random.choice(arr)


head = ListNode()
head.next = ListNode(10)
head.next.next = ListNode(100)
print(head.val)
print(head.next.val)
print(head.next.next.val)


s = Solution(head)
print(s.getRandom())

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head

    dummy = ListNode()
    dummy.next = head
    pre = None
    cur = dummy

    for _ in range(left):
        pre = cur
        cur = cur.next

    pre2 = pre
    cur2 = cur

    for i in range(right - left + 1):  # 这里实际要进行3次操作，所以要加1
        print('i', i)
        print('cur', cur.val)
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    cur2.next = cur
    pre2.next = pre
    return dummy.next




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reverseBetween(head, 2, 4)

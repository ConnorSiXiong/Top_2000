class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode(head: ListNode) -> ListNode:
    index = 1
    current = head

    while current.next is not None:
        current = current.next
        index += 1

    for i in range(index // 2):
        head = head.next
    return head


def middleNode2(head: ListNode) -> ListNode:
    cur = head
    count = 1
    index = {}

    while cur.next is not None:
        index[count] = cur
        cur = cur.next
        count += 1

    return index[count//2]


# a = ListNode(1)
#
# current_node = a
#
# for i in range(2,10):
#     new_node = ListNode(i)
#     current_node.next = new_node
#     current_node = new_node
#
# b = middleNode(a)
#
# print(b.next.next.val)
#
# print('00')
# print(2//2)
# print(3//2)
# print(4//2)
# print(5//2)
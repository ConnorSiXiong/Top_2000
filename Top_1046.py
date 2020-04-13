import bisect
import heapq

from typing import List


def lastStoneWeight(self, stones: List[int]) -> int:
    heap = [-x for x in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        big = heapq.heappop(heap)
        small = heapq.heappop(heap)

        new_weight = big - small

        if new_weight != 0:
            heapq.heappush(heap, new_weight)

    if len(heap):
        return -heap[0]
    else:
        return 0


def lastStoneWeight2(self, A):
    h = [-x for x in A]
    heapq.heapify(h)
    while len(h) > 1 and h[0] != 0:
        heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
    return -h[0]


def lastStoneWeight3(self, A):
    A.sort()
    while len(A) > 1:
        bisect.insort(A, A.pop() - A.pop())
    return A[0]


a = [9, 1, 2, 5, 3, 4]
print(a)

heap = [-x for x in a]
heapq.heapify(heap)

print(heap)


for i in range(len(a)):
    if i == 0:
        print('[', heapq.heappop(heap), sep='', end=', ')
    elif i != len(a) - 1:
        print(heapq.heappop(heap), end=', ')
    else:
        print(heapq.heappop(heap), end='] ')

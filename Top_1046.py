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


a = [9,1,2,5,3,4]
print(a)

heap = [-x for x in a]
heapq.heapify(heap)

print(heap)

for i in range(len(a)):
    print(heapq.heappop(heap))

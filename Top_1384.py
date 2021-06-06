from heapq import heappush, heappop
from typing import List


def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    speed_heap = []
    speed_sum = 0
    res = 0
    q = sorted(zip(efficiency, speed), reverse=True)
    for cur_efficiency, cur_speed in q:
        # print('cur_efficiency', cur_efficiency)
        # print('cur_speed', cur_speed)
        heappush(speed_heap, cur_speed)
        speed_sum += cur_speed
        if k < len(speed_heap):
            speed_sum -= heappop(speed_heap)
        res = max(res, speed_sum * cur_efficiency)
    return res % (10 ** 9 + 7)


n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 3

print(maxPerformance(n, speed, efficiency, k))

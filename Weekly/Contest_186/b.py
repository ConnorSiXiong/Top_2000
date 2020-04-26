import heapq
from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    """

    1 <= cardPoints.length <= 10^5
    1 <= cardPoints[i] <= 10^4
    1 <= k <= cardPoints.length

    """
    if k == 1:
        return max(cardPoints[0], cardPoints[-1])
    if k == len(cardPoints):
        return sum(cardPoints)

    k = k - 1
    # left
    left_rest_points = cardPoints[1:]
    hp = [-x for x in left_rest_points[:k]]  # 保持k个数的大根堆
    heapq.heapify(hp)
    for i in range(k, len(left_rest_points)):  # 从k开始遍历
        if -hp[0] <= left_rest_points[i]:  # 检查大根堆中最大的数 是否 大于其他数
            heapq.heappop(hp)
            heapq.heappush(hp, left_rest_points[i])

    left_result = sum(hp) + cardPoints[0]

    right_rest_points = cardPoints[:-1]
    hp = [x for x in right_rest_points[:k]]  # 保持k个数的大根堆
    heapq.heapify(hp)
    for i in range(k, len(right_rest_points)):  # 从k开始遍历
        if hp[0] <= right_rest_points[i]:  # 检查大根堆中最大的数 是否 大于其他数
            heapq.heappop(hp)
            heapq.heappush(hp, right_rest_points[i])

    right_result = sum(hp) + cardPoints[-1]
    return max(right_result, left_result)


def maxScore2(cardPoints: List[int], k: int) -> int:
    result = sum(cardPoints[:k])
    current = sum(cardPoints[:k])

    for i in range(k):
        current -= cardPoints[k-i-1]
        current += cardPoints[-i-1]
        result = max(result, current)
    return result


a = [1,79,80,1,1,1,200,1]
k = 3
print(maxScore2(a, k))



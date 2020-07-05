import heapq


def nthUglyNumber(n: int) -> int:
    """
    一开始理解错了
    只能包含1，2，3，5不能包含其他因数
    """
    result = 1
    heap = [1]
    visited = {1}

    for i in range(n):
        result = heapq.heappop(heap)

        for i in [2, 3, 5]:
            if result * i not in visited:
                heapq.heappush(heap, result * i)
                visited.add(result * i)

    return result

print(nthUglyNumber(11))

from typing import List


def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    """
    1 <= intervals.length <= 1000
    intervals[i].length == 2
    0 <= intervals[i][0] < intervals[i][1] <= 10^5
    """
    intervals.sort()
    result = []

    first = intervals[0]
    result.append(first)
    for i in range(1, len(intervals)):
        pre = result[-1]
        cur = intervals[i]

        pre_head = pre[0]
        pre_tail = pre[1]

        cur_head = cur[0]
        cur_tail = cur[1]

        if cur_head == pre_head:
            if cur_tail <= pre_tail:
                continue
            else:
                result.pop()
                result.append(cur)
        else:
            # cur_head > pre_head
            if cur_tail <= pre_tail:
                continue
            else:
                result.append(cur)

    return result


a = [[1, 4], [3, 6], [2, 8]]
b = [[99, 110], [99, 100], [1, 2], [1, 4], [3, 4]]

print(removeCoveredIntervals(b))

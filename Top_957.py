from typing import List


def prisonAfterNDays(cells: List[int], N: int) -> List[int]:
    dic = {}
    while N > 0:
        dic[''.join(map(str, cells))] = N
        N -= 1
        tmp = [0] * 8
        for i in range(1, 7):
            tmp[i] = 1 if cells[i - 1] == cells[i + 1] else 0
        cells = tmp
        t = ''.join(map(str, cells))
        if t in dic:
            N = N % (dic[t] - N)
    return cells
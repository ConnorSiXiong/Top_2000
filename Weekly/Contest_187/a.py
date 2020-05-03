from typing import List


def destCity(paths: List[List[str]]) -> str:
    l = len(paths)

    if l == 1:
        return paths[0][1]
    else:
        start = []
        end = []

        for i in range(l):
            current_path = paths[i]
            A = current_path[0]
            B = current_path[1]
            start.append(A)
            end.append(B)

    for i in end:
        if i not in start:
            return i


paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths2 = [["B","C"],["D","B"],["C","A"]]
paths3 = [["A","Z"]]
print(destCity(paths3))




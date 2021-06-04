import collections

DIRECTIONS = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, -2),
    (-1, 2)
]


def minKnightMoves_BFS(x: int, y: int):
    target = (x, y)

    q = collections.deque([])
    q.append([(0, 0), 0])
    visited = set()

    while q:
        position, step = q.popleft()

        if isArrive(position, target):
            return step

        # visited.add((position))  # 不能在这个地方添加
        x = position[0]
        y = position[1]

        for dx, dy in DIRECTIONS:
            next_x = x + dx
            next_y = y + dy
            if (next_x, next_y) in visited:
                continue
            q.append([(next_x, next_y), step + 1])
            visited.add((next_x, next_y))
    return -1


def isArrive(position, target):
    if abs(position[0]) == abs(target[0]) and abs(position[1]) == abs(target[1]):
        return True
    return False
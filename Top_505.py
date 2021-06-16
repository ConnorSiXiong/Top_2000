import heapq
from typing import List
import numpy as np
from collections import deque


def shortestDistance(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    start, destination = tuple(start), tuple(destination)
    row_size = len(maze)
    col_size = len(maze[0])

    def neighbors(maze, node):
        temp = []
        used = set()
        used.add(node)
        for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            (x, y), dist = node, 0
            while 0 <= x + dx < row_size and 0 <= y + dy < col_size and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                dist += 1
            if (x, y) not in used:
                temp.append((dist, (x, y)))
        return temp

    heap = [(0, start)]
    visited = set()
    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited: continue
        if node == destination:
            return dist
        visited.add(node)
        for neighbor_dist, neighbor in neighbors(maze, node):
            heapq.heappush(heap, (dist + neighbor_dist, neighbor))

    return -1


def shortestDistance2(maze, start, destination) -> int:
    maze = np.array(maze)

    start = tuple(start)
    destination = tuple(destination)

    if start == destination:
        return 0

    visited = set()
    visited.add(start)

    q = deque([])
    q.append([start, 0])

    while q:
        cur_position, steps = q.popleft()

        if cur_position == destination:
            return steps

        for next_movement in getNextMovement(maze, cur_position, visited):
            next_position, sub_steps = next_movement
            q.append([next_position, steps + sub_steps])
    return -1


D = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def getNextMovement(maze, position, visited):
    rows = maze.shape[0]
    cols = maze.shape[1]
    res = []

    for dx, dy in D:
        x, y = position
        sub_steps = 0
        while 0 <= x + dx < cols and 0 <= y + dy < rows and maze[x + dx, y + dy] == 0:
            x += dx
            y += dy
            sub_steps += 1
        if (x, y) in visited:
            continue
        res.append([(x, y), sub_steps])
        visited.add((x, y))
    return res


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(shortestDistance2(maze, start, destination))
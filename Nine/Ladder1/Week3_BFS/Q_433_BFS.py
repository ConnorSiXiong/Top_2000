import collections

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    res = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] and (i, j) not in visited:
                bfs(grid, visited, i, j)
                res += 1

    return res


def bfs(grid, visited, x, y):
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            next_x = x + dx
            next_y = y + dy
            if not isValid(grid, visited, next_x, next_y):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))


def isValid(grid, visited, x, y):
    cols = len(grid)
    rows = len(grid[0])

    if not (0 <= x < cols and 0 <= y < rows):
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] == 0:
        return False
    return True


a = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
]
print(numIslands(a))


def numIslands2(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 or (i, j) in visited:
                continue
            bfs(grid, visited, i, j)
            res += 1
    return res


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs2(grid, visited, x, y):
    q = collections.deque()
    q.append([x, y])
    visited.add((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy
            if isValid(grid, visited, next_x, next_y):
                continue
            q.append([next_x, next_y])
            visited.add((next_x, next_y))


def isValid2(grid, visited, x, y):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return False
    if grid[x][y] == 1:
        return False
    if visited[x][y] == 1:
        return False
    return True


print(numIslands2(a))

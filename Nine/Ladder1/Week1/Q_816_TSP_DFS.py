cities = [[1, 2, 1], [2, 3, 2], [1, 3, 3]]
n = 3


class Result:
    def __init__(self):
        self.min_cost = float('inf')


def construct_graph(roads, n):
    graph = {
        i: {j: float('inf') for j in range(1, n + 1)}
        for i in range(1, n + 1)
    }

    for a, b, c in roads:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    return graph


print(construct_graph([[1, 2, 1], [2, 3, 2], [1, 3, 3]], 3))


def minCost(roads, n):
    graph = construct_graph(roads, n)
    res = Result()
    dfs(1, n, {1}, 0, graph, res)
    return res.min_cost


def dfs(city, n, visited, cost, graph, res):
    if len(visited) == n:
        res.min_cost = min(res.min_cost, cost)
        return

    for next_city in graph[city]:
        if next_city in visited:
            continue
        visited.add(next_city)
        dfs(next_city, n, visited, cost + graph[city][next_city], graph, res)
        visited.remove(next_city)


print(minCost(cities, n))

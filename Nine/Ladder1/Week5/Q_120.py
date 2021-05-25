def minimumTotal(arr):
    return dc(arr, 0, 0, {})


def dc(arr, x, y, memo):
    if len(arr) == x:
        return 0

    if (x, y) in memo:
        return memo[(x, y)]

    left = dc(arr, x + 1, y, memo)
    right = dc(arr, x + 1, y + 1, memo)

    memo[(x, y)] = min(left, right) + arr[x][y]
    return memo[(x, y)]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

print(minimumTotal(triangle))


def minimumTotal2(arr):
    # 自底向上

    # dp[i][j] 代表从i，j走到最底层的最短路径值
    n = len(arr)

    # 状态
    dp = [[0] * (i + 1) for i in range(n)]

    # 初始化
    for i in range(n):
        dp[n-1][i] = arr[n-1][i]

    # 自底向上开始推导
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + arr[i][j]

    return dp[0][0]

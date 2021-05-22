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


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(minimumTotal(triangle))
def minimumTotal(arr):
    return divideConquer(arr, 0, 0, {})


def divideConquer(arr, x, y, memo):
    if x == len(arr):
        return 0

    if (x, y) in memo:
        return memo[(x, y)]

    left = divideConquer(arr, x + 1, y, memo)
    right = divideConquer(arr, x + 1, y + 1, memo)
    memo[(x, y)] = min(left, right) + arr[x][y]

    return memo[(x, y)]

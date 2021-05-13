def kClosestNumbers(arr, target, k):
    if len(arr) == 0:
        return []

    res = []
    right = findIndex(arr, target)
    left = right - 1

    for _ in range(k):
        if isLeftCloser(arr, left, right, target):
            res.append(arr[left])
            left -= 1
        else:
            res.append(arr[right])
            right += 1
    return res


def findIndex(arr, target):
    left = 0
    right = len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid
        else:
            right = mid

    if arr[left] >= target:
        return left
    if arr[right] >= target:
        return right
    return len(arr)


def isLeftCloser(arr, left, right, target):
    if right >= len(arr):
        return True
    if left < 0:
        return False

    if abs(arr[left] - target) <= abs(arr[right] - target):
        return True
    return False


arr = [1, 4, 6, 8]
print(kClosestNumbers(arr, 3, 3))

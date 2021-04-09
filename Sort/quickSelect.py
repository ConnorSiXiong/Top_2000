# 从list里面找第 k 大的元素


def qs(arr, k):
    if len(arr) == 0:
        return None
    if k <= 0 or k > len(arr):
        return None

    k = len(arr) - k
    return qs2(arr, 0, len(arr) - 1, k)


def qs2(arr, start, end, k):
    left = start
    right = end

    pivot = arr[(start + end) // 2]

    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    if k <= right:
        qs2(arr, start, right, k)

    if k >= left:
        qs2(arr, left, end, k)
    return arr[k]


a = [5, 4, 3, 1, 2]
k = 1

print(qs(a, k))

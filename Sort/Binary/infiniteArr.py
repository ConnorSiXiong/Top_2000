def binary_search(arr, start, end, target):
    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid
        else:
            end = mid
    if arr[start] == target:
        return start
    if arr[end] == target:
        return end
    return -1


def expand_arr(arr, target):
    index = 1
    while arr[index - 1] < target:
        index *= 2
    return index


def infiniteArrSearch(arr, target):
    if len(arr) == 0:
        return -1
    start = 0
    end = expand_arr(arr, target)
    return binary_search(arr, start, end, target)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(infiniteArrSearch(arr, 4))
def merge1(arr):
    temp = [-1] * len(arr)
    merge2(arr, 0, len(arr) - 1, temp)
    print(arr)


def merge2(arr, start, end, temp):
    if start >= end:
        return

    mid = (start + end) // 2
    merge2(arr, start, mid, temp)
    merge2(arr, mid + 1, end, temp)
    merge(arr, start, end, temp)


def merge(arr, start, end, temp):
    mid = (start + end) // 2
    left_start = start
    right_start = mid + 1
    index = left_start

    while left_start <= mid and right_start <= end:
        if arr[left_start] < arr[right_start]:
            temp[index] = arr[left_start]
            index += 1
            left_start += 1
        else:
            temp[index] = arr[right_start]
            index += 1
            right_start += 1

    while left_start <= mid:
        temp[index] = arr[left_start]
        index += 1
        left_start += 1
    while right_start <= end:
        temp[index] = arr[right_start]
        index += 1
        right_start += 1

    for i in range(start, end+1):
        arr[i] = temp[i]


a = [1, 10, 2, 3, 0, 7, 8, 9]
merge1(a)

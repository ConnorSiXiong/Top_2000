def binary(arr, target):
    # 在数组里找到特定的数
    if len(arr) == 0:
        return -1

    start = 0
    end = len(arr) - 1

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


test_arr = [1, 2, 3, 4, 5, 6]
for i in range(5):
    print(binary(test_arr, i))

print(binary(test_arr, 6))
print(binary(test_arr, 10))
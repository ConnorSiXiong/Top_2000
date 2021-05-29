arr0 = [-2, -1, 1, 2, 3, 4, 5]
arr1 = [1, 1, 1, 10, 10, 10]
arr2 = [-2, -1, 1, 2, 3, 4, 5]
arr3 = [5, 7, 7, 8, 8, 10]


def findClosestElements(arr, target, k):
    arr = sorted(arr)

    right = findIndex(arr, target)
    print('right', right)
    if right < 0:
        return []
    left = right - 1
    res = []
    for _ in range(k):
        if checkLeftCloser(arr, left, right, target):
            res.append(arr[left])
            left -= 1
        else:
            res.append(arr[right])
            right += 1
    return sorted(res)


def findIndex(arr, target):
    # OXXXX
    # get the first X > target
    left = 0
    right = len(arr) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid

    if arr[left] > target:
        return left
    if arr[right] > target:
        return right
    return -1


def checkLeftCloser(arr, left, right, target):
    if left < 0:
        return False
    if right >= len(arr):
        return True
    if abs(arr[left] - target) <= abs(arr[right] - target):
        return True
    return False


# print(findClosestElements(arr3, 9, 3))


def minimumAbsDifference(arr):
    dic = dict()
    arr = sorted(arr)
    min_val = float('inf')
    for i in range(1, len(arr)):
        key_val = arr[i] - arr[i - 1]

        if key_val < min_val:
            min_val = key_val

        if key_val not in dic:
            dic[key_val] = [[arr[i - 1], arr[i]]]
        else:
            temp = dic[key_val]
            temp.append([arr[i - 1], arr[i]])
            dic[key_val] = temp
    return dic[min_val]


print(minimumAbsDifference([4, 2, 1, 3]))

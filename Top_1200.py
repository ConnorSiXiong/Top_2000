def minimumAbsDifference(arr):
    arr = sorted(arr)
    print(arr)
    min_val = arr[1] - arr[0]

    res = []
    for i in range(1, len(arr)):
        cur = arr[i] - arr[i - 1]
        if cur < min_val:
            min_val = cur
            res = [[arr[i - 1], arr[i]]]
        elif cur == min_val:
            res.append([arr[i - 1], arr[i]])
    return res


def minimumAbsDifference2(arr):
    # hashmap
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


print(minimumAbsDifference([40, 11, 26, 27, -20]))

def partitionArray(nums, k):
    if len(nums) == 0:
        return 0
    big = 0
    small = 0
    for i in nums:
        if i >= k:
            big += 1
        else:
            small += 1
    return small

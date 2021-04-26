# -------------------
# ----- 方法 1 -------
# -------------------
# def search(nums, target):
#     start = 0
#     end = len(nums) - 1
#     if len(nums) == 0:
#         return -1
#
#     if len(nums) == 1 and target != nums[0]:
#         return -1
#
#     min_index = get_min_index(nums)
#     print(min_index)
#
#     if nums[min_index] == target:
#         return min_index
#
#     # if nums[min_index] <= target:
#     # 这个地方一开始没有加右边界
#     # 那么在原数组全降序的时候，
#     # [3, 2, 1]
#
#     # 当 target = 3时
#     # min_index = 2
#     # (nums[2] = 1) <= (target = 3)
#     # 然后直接进入右边就找不到了
#     # get_target_index(nums, min_index = 2, end = 2, target = 3)
#     # min_index 和 end重合了
#
#     if nums[min_index] <= target <= nums[-1]:
#         print('右边')
#         return get_target_index(nums, min_index, end, target)
#     else:
#         print('左边')
#         return get_target_index(nums, start, min_index - 1, target)
#
#
# def get_min_index(arr):
#     start, end = 0, len(arr) - 1
#
#     while start + 1 < end:
#         mid = (start + end) // 2
#         if arr[mid] < arr[end]:
#             end = mid
#         else:
#             start = mid
#     return start if arr[start] < arr[end] else end
#
#
# def get_target_index(arr, start, end, target):
#     print('start', start)
#     print('end', end)
#     while start + 1 < end:
#         mid = (start + end) // 2
#
#         if arr[mid] < target:
#             start = mid
#         else:
#             end = mid
#     if arr[start] == target:
#         return start
#     if arr[end] == target:
#         return end
#     return -1
#
#

def search(arr, target):
    if len(arr) == 0:
        return -1
    if len(arr) == 1 and arr[0] != target:
        return -1

    start = 0
    end = len(arr) - 1

    min_index = find_min_index(arr)
    if arr[min_index] == target:
        return min_index

    if arr[min_index] <= target <= arr[-1]:
        return find_target(arr, target, min_index + 1, end)
    else:
        return find_target(arr, target, start, min_index - 1)


def find_min_index(arr):
    start = 0
    end = len(arr) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] < nums[end]:
            end = mid
        else:
            start = mid
    return start if arr[start] < arr[end] else end


def find_target(arr, target, start, end):
    while start + 1 < end:
        mid = (start + end) // 2
        if target < arr[mid]:
            end = mid
        else:
            start = mid

    if arr[start] == target:
        return start
    if arr[end] == target:
        return end
    return -1


nums = [1,1,1,0]
print(find_min_index(nums))
# t = 1
#
# print(search(nums, t))

# -------------------
# ----- 方法 2 -------
# -------------------
# def search(nums, target):
#     if nums is None or len(nums) == 0:
#         return -1
#
#     if len(nums) == 1 and target != nums[0]:
#         return -1
#
#     start, end = 0, len(nums) - 1
#
#     while start + 1 < end:
#         mid = (start + end) // 2
#         # 左边
#         if nums[mid] >= nums[start]:
#             if nums[start] <= target <= nums[mid]:
#                 end = mid
#             else:
#                 start = mid
#         else:
#             if nums[mid] <= target <= nums[end]:
#                 start = mid
#             else:
#                 end = mid
#
#     if nums[start] == target:
#         return start
#     if nums[end] == target:
#         return end
#     return -1
#
#
# nums = [3, 2, 1]
# target = 1
# print(search(nums, target))

# -------------------
# ----- 方法 3 -------
# -------------------

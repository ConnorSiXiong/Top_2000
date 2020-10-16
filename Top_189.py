from typing import List


def rotate(nums: List[int], k: int) -> None:
    if k == 0 or len(nums) == 1:
        return

    k = k % len(nums)

    def my_reverse(left, right):
        nonlocal nums

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    my_reverse(0, len(nums) - 1)
    my_reverse(0, k - 1)
    my_reverse(k, len(nums) - 1)
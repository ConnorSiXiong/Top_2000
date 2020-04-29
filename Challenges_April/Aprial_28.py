import collections
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = collections.Counter(nums)
        self.current = 0
        self.nums = nums

    def showFirstUnique(self) -> int:
        while self.current < len(self.nums):
            if self.count[self.nums[self.current]] == 1:
                return self.nums[self.current]
            self.current += 1
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value not in self.count:
            self.count[value] = 1
        else:
            self.count[value] += 1
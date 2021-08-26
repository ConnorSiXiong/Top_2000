"""
一个简单的便利，练手

Author: Alex
Date: 26/08/2021 - NZ Auckland
      20:54 - 21:05

      思路：
      traverse arr, record the indexes of target words

      出现一个bug，distance初始值错了，应该是最大值
"""
from typing import List


class Solution:
    def shortestDistance(self, arr: List[str], a: str, b: str) -> int:
        distance = float('inf')
        index1 = -1
        index2 = -1

        for i in range(len(arr)):
            cur = arr[i]
            if cur == a:
                index1 = i
            if cur == b:
                index2 = i
            if index1 != -1 and index2 != -1:
                distance = min(distance, abs(index2 - index1))
        return distance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "makes"

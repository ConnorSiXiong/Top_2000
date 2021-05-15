# 203

import math


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, arr, k):
        if len(arr) == 0:
            return 0

        # write your code here
        left = 1
        """
            1. 一开始写的是min
            但是这个案例会无法通过
            
            arr = [511, 877, 644, 610, 919, 5734, 148, 968, 672, 637, 971, 501, 305, 152, 437, 446, 201, 464, 312, 163, 
                   302, 2392, 7431, 876, 978, 995]
            k = 128
            
            2. 不是max+1的话，不切的无法得到
            [200, 200, 200], k = 3
            会切出来199
        """
        right = max(arr) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            pieces = self.cutPieces(arr, mid)
            if pieces >= k:
                left = mid
            else:
                right = mid
        if self.cutPieces(arr, left) >= k:
            return left
        if self.cutPieces(arr, right) >= k:
            return right

        return 0

    def cutPieces(self, arr, cut_len):
        pieces = 0
        for i in arr:
            pieces += math.floor(i / cut_len)
        return pieces

from typing import List

s = "dsahjpjauf"
w = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]

# s = "qlhxagxdqh"
# w = ["qlhxagxdq", "qlhxagxdq", "lhyiftwtut", "yfzwraahab"]

#
# s = "abcbe"
# w = ["bbb"]
# w = ["a", "bb", "acd", "ace"]

def numMatchingSubseq( s: str, words: List[str]) -> int:
    """
        1. initiate the hashmap
        2. fill the hashmap

        3. whether each word match ?

    """
    # 1. initiate
    hashmap = {chr(i + ord('a')): [] for i in range(26)}

    # 2. fill out
    for idx, c in enumerate(s):
        hashmap[c].append(idx)
    # 3. matchable ?
    count = 0
    for i in words:
        if match(i, hashmap):
            count += 1

    return count

def match(word, hashmap):
    find_after_index = -1
    """
        这个find after是指在原s里的位置
        
        比如：
        s = abcddbc
            0123456
            
        target = "cbc"
        
        c : [2, 6]
        b : [1, 5]
        
        
        binaryFind 找到第一个c，在hashmap里的index是0，通过这个index，可以确定它在s中的index是2
        下一次查找都要在s里的它当前的index 2之后，
        
        也就是----下一次从index 3开始找
        
        所以，是确定它在s里的index
    """
    for c in word:
        """
            1. find its positions in 原字符串s
        """
        position_arr = hashmap[c]

        """
            2. 找到它当前正在用的，在hashmap里的 index
            如果二分法在hashmap的位置arr里找不到，就说明它不存在，那么返回false
            如果找到了，就说明它使用的是s里位置是position_arr[index]的那一个char
            
        """
        index = binaryFind(position_arr, find_after_index+1)
        if index == -1:
            return False
        find_after_index = position_arr[index]  # 关键这一步
    return True


def binaryFind(arr, val):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            left = mid
        else:
            right = mid

    if arr[left] >= val:
        return left

    if arr[right] >= val:
        return right

    return -1

print(numMatchingSubseq(s, w))
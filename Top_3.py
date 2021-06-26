s = "pbavjvkkmvjk"
s = 'abcabcdefg'

def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)
    i = 0
    j = 1
    res = 0
    while i < len(s) - 1 and j < len(s):
        longest = s[i:j]
        res = max(len(longest), res)
        while s[j] in longest and i <= j:
            #  这个while循环作用于 "kabcdefjkj"
            #  把第一个k跳过
            i += 1
            longest = s[i:j]
        j += 1
    longest = s[i:j]  # 这个是因为字符串的最后一个位置访问不到
    res = max(len(longest), res)
    return res


lengthOfLongestSubstring(s)

# s = 'abcabcdefg'
def lengthOfLongestSubstring2(s: str) -> int:
    characters = set()
    left = 0
    right = 0
    ans = 0
    length = len(s)

    while right < length:
        if s[right] in characters:
            characters.remove(s[left])
            left += 1
        else:
            characters.add(s[right])
            right += 1
            ans = max(ans, right - left)

    return ans


def lengthOfLongestSubstring3(s):
    # 在自己写的第一版本上做了最后计算结果的更新
    if len(s) <= 1:
        return len(s)
    i = 0
    j = 1
    res = 0
    while i < len(s) - 1 and j < len(s):
        longest = s[i:j]
        # 主要是把计算res放到while循环里面来了，放到最后计算
        # 之前的写法是放在开头计算
        # 如果放在开头计算
        # 那么最后一个j+1到最后一个位置就没法算了，到最后一个位置( j == len(s)-1 )会发生s[j] out of index

        # 这个能放在while里面循环的另外一个原因就是
        # if里面的while，把切片数组里最前面重复的s[j]给去掉了，保证了切片数组里一定没有重复的东西
        # 所以能放在底下更新res

        # 这个if else去掉也行
        # 方便理解
        if s[j] in longest:
            while s[j] in longest and i <= j:
                i += 1
                longest = s[i:j]
        else:
            j += 1
        res = max(j-i, res)

    return res


def lengthOfLongestSubstring4(s):
    """
    2021.06.27
    这种求 substring 的
    往sliding window那个方向靠

    然后这种的题，用while处理好像比用for处理更容易

    o(2n) = o(n)
    """
    comb = set()

    left = 0
    right = 0

    res = 0
    while right < len(s):
        if s[right] in comb:
            # a b c d c c
            # 如果当前有重复的，会一直清空，知道清空到没有（在这个例子里就是清空到当前位置）为止
            comb.remove(s[left])
            left += 1
        else:
            comb.add(s[right])
            right += 1

            res = max(res, right - left)
    return res




print(lengthOfLongestSubstring2(s))
print(lengthOfLongestSubstring4(s))
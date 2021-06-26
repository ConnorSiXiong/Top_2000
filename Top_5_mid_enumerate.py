def longestPalindrome(s: str) -> str:
    res = ""
    print('len', len(s))
    for i in range(len(s)):
        ans1 = midExpand(s, i, i)
        ans2 = midExpand(s, i, i + 1)

        if len(ans1) > len(res):
            res = ans1
        if len(ans2) > len(res):
            res = ans2
        max_len = len(res)

        if max_len >= len(s) - i:
            break
    return res


def midExpand(s, left, right):
    # while 循环最后一轮会多运算一次
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1: right]


"""
这样写就卡在循环里出不去了

上面的写法还不用再考虑奇数偶数的问题

def midExpand(s, left, right):
    while left >= 0 and right < len(s) :
        if s[left] == s[right]:
            left -= 1
            right += 1
    return right - left - 1
    
如果要跳出循环得加一条

if s[left] != s[right]:
    break
"""

print(longestPalindrome("aaaaa"))

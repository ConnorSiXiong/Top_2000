s = "pbavjvkkmvjk"


# s = "abcabcbb"

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
            i += 1
            longest = s[i:j]
        j += 1
    longest = s[i:j]
    res = max(len(longest), res)
    return res

lengthOfLongestSubstring(s)

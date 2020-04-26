def maxScore(s: str) -> int:

    s = list(s)
    result = 0
    for i in range(1, len(s)):
        zero_n = 0
        one_n = 0
        left = s[0:i]
        right = s[i:]
        for zero in left:
            if zero == '0':
                zero_n += 1
        for one in right:
            if one == '1':
                one_n += 1
        result = max(result, zero_n + one_n)
    return result


s = "011101"
s = list(s)
left = s[0:1]
right = s[1:]
print(s)
print(left)
print(right)

print(maxScore(s))

"""
9 min
"""
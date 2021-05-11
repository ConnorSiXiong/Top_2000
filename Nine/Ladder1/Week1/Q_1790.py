def RotateString2(s, left, right):
    # write your code here
    if len(s) <= 1 or left == right:
        return s

    if left > right:
        offset = (left - right) % len(s)

    else:
        offset = (right - left) % len(s)
        offset = len(s) - offset
    return s[offset:] + s[:offset]


print(RotateString2("abcdefg", 3, 1))

print("abcdefg"[:2])
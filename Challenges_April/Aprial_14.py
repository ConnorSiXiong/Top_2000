import collections
from typing import List


def stringShift(self, s: str, shift: List[List[int]]) -> str:
    count = 0

    for i in shift:
        direction, amount = i
        if direction:
            count += amount
        else:
            count -= amount

    amount = abs(count) % len(s)
    if amount == 0:
        return s

    if count > 0:
        return rightShift(s, amount)
    else:
        return leftShift(s, amount)

# 写一个向左平移的 method
def rightShift(s: str, length: int) -> str:
    left_part = s[0: len(s) - length]
    right_part = s[len(s) - length: len(s)]
    left_part = left_part[::-1]
    right_part = right_part[::-1]
    return (left_part + right_part)[::-1]


def leftShift(s: str, length: int) -> str:
    left_part = s[0: length]
    right_part = s[length: len(s)]
    left_part = left_part[::-1]
    right_part = right_part[::-1]
    return (left_part + right_part)[::-1]

"""
[方向，移动量]
0 左边
1 右边
"""

a = "abcde"

amount = abs(5) % len(a)



def stringShift2(s: str, shift: List[List[int]]) -> str:
    chars = collections.deque(s)
    for d, amount in shift:
        if d == 0:
            for _ in range(amount):
                num = chars.popleft()
                chars.append(num)
        else:
            for _ in range(amount):
                num = chars.pop()
                chars.appendleft(num)
    return ''.join(chars)


def stringShift3(s: str, shift: List[List[int]]) -> str:
    left = 0
    for d, a in shift:
        if d:
            left -= a
        else:
            left += a
    print(left)
    left %= len(s)  # 如何处理 负数整数的除法 的 余数
    print(left)

    return s[left:] + s[:left]

a = "abcde"
shift = [[0,1],[0,1],[1,10],[1,3]]

stringShift3(a, shift)
print(a[2:])
print(a[:2])

print(-11%5)
print(-11//5)

# -11 除以 5 = -3 ... 4
# 余数必须是正数
# - 余数是一个小于除数的非零自然数
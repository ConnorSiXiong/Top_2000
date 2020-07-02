def arrangeCoins(n: int) -> int:
    level = 1
    i = 1
    while True:
        n = n - i
        if n < 0:
            return level - 1
        if n == 0:
            return level
        i += 1
        level += 1

print(arrangeCoins(4))
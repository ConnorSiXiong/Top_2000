def hammingDistance(x: int, y: int) -> int:
    x = bin(x)[2:]
    y = bin(y)[2:]
    counter = 0

    if len(x) >= len(y):
        long_len = len(x)
        y = '0' * (len(x) - len(y)) + y
    else:
        long_len = len(y)
        x = '0' * (len(y) - len(x)) + x
    for i in range(long_len):
        if int(x[i]) ^ int(y[i]) != 0:
            counter += 1

    return counter


def hammingDistance2(x: int, y: int) -> int:
    if x == y:
        return 0
    else:
        z = x ^ y
        z = bin(z)
        return z.count('1')
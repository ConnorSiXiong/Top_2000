def numberOfSteps(num: int) -> int:
    """
    当输入特别大的时候，这个办法就不管用了
    """
    if num == 0:
        return 0
    times = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1

        times += 1
    times += 1
    return times


def numberOfSteps2(num: int) -> int:
    s = bin(num)[2:]
    print('s', s)
    return s.count('1') + len(s) - 1


a = 14

print(numberOfSteps2(14))

print(14&1)
print(13&1)
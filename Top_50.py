# 二分法
# Reference：
# https://www.bilibili.com/video/BV1mt411M712?from=search&seid=4220438892334117585


def myPow(x: float, n: int) -> float:
    if x == 1:
        return 1
    if n == 0:
        return 1
    if x == 0:
        return 0

    negative = False
    if n < 0:
        n = -n
        negative = True

    side = 1

    while n != 1:
        # 这个代表有奇数个次方

        if n % 2 != 0:
            # 不能写 side = 1 * x
            # 不然不能通过 n = 7
            # round 1, n = 7
            # round 2, n = 3
            side = side * x
        x = x * x
        n = n // 2

    x = x * side

    if negative:
        x = 1/x

    return x


print(myPow(2, -2147483648))



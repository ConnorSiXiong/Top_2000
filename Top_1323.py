def maximum69Number(num: int) -> int:
    num = list(str(num))
    for i in range(len(num)):
        cur = num[i]
        if cur == '6':

            num[i] = '9'
            break
    return int("".join(num))

def addDigits(num: int) -> int:
    if num < 10:
        return num
    while num >= 10:
        num = str(num)
        result = 0

        for i in num:
            result += int(i)
        if result / 10 < 1:
            return result
        num = result


print(addDigits(19))

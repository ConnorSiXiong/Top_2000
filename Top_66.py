from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if len(digits) == 1:
        if digits[0] != 9:
            digits[0] += 1
            return digits
        else:
            return [1, 0]

    for i in reversed(range(len(digits))):
        if i != 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        else:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:

                digits[i] = 0

                digits = [1] + digits
                return digits


def plusOne2(digits: List[int]) -> List[int]:
    for i in reversed(range(len(digits))):
        print(i)
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    if digits[0] == 0:
        digits = [1] + digits
    return digits


a = [1,2,3]

print(plusOne2(a))
"""
2020.04.07

Input: "the sky is blue"
Output: "blue is sky the"

"""


def reverseWords(s: str) -> str:
    return ' '.join(one[::-1] for one in s[::-1].strip().split())


def reverseWords2(s: str) -> str:
    a = s.split()
    # print(a)
    # print(a[::-1])
    y = ' '.join(a[::-1])
    return y


if __name__ == '__main__':
    str1 = 'the sky is blue '
    b = reverseWords2(str1)
    print(b)
    # print(str[::-1])
    # print(str[::-1].strip())
    # arr2 = str[::-1].strip().split()
    # print(arr2)
    # arr3 = [word[::-1] for word in arr2]
    # print(arr3)

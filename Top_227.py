def calculate(s: str) -> int:
    s = s.replace(' ', '')
    operators1 = ['*', '/']
    operators2 = ['+', '-']

    operators = operators1 + operators2

    arr = []
    pre = 0
    for index in range(len(s)):
        cur = s[index]
        if cur in operators:
            component = s[pre: index]
            pre = index + 1
            arr.append(component)
            arr.append(cur)

        if index == len(s) - 1:
            arr.append(s[pre: index + 1])

    while '*' in arr or '/' in arr:
        for i in range(1, len(arr) - 1):

            cur = arr[i]

            if cur in operators1:
                pre = arr[i - 1]
                next = arr[i + 1]
                if cur == '*':
                    cur = int(pre) * int(next)
                else:
                    cur = int(int(pre) / int(next))

                arr[i] = cur

                del arr[i + 1]
                del arr[i - 1]
                break
            else:
                continue

    while len(arr) != 1:
        for i in range(1, len(arr) - 1):
            cur = arr[i]
            if cur in operators2:
                pre = arr[i - 1]
                next = arr[i + 1]
                if cur == '+':
                    cur = int(pre) + int(next)
                else:
                    cur = int(pre) - int(next)

                arr[i] = cur

                del arr[i + 1]
                del arr[i - 1]
                break
    return arr[0]


s1 = "3+2*2"
a1 = 7

s2 = " 3/2 "
a2 = 1

s3 = " 3+5 / 2 "
a3 = 5

s4 = " 111111         + 1 + 10 * 1"
a4 = 111112

s5 = '0-0'

print(calculate(s5))

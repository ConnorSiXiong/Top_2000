def numSteps(s: str) -> int:
    # 1101 -> 1110 -> 111 -> 1000 -> 100 -> 10 -> 1

    # ⚠️注意这个递归终止条件
    if s == '1':
        return 0

    if s[-1] == '0':
        return 1 + numSteps(s[0:-1])
    else:
        zero_index = s.rfind('0')

        if zero_index == -1:
            s = '1' + '0' * len(s)
            return 1 + numSteps(s)
        else:
            # 11011 -> 1110
            # 这个地方我操作了两次，所以 +2
            s = s[0: zero_index] + '1' + '0' * (len(s) - zero_index - 2)
            return 2 + numSteps(s)


a = "10"
# 1110

print(numSteps(a))

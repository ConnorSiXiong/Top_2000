from time import sleep
import pprint
phone = {
    # '2': ['a', 'b'],
    # '3': ['d', 'e'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        }


def letterCombinations(digits):
    if len(digits) == 0:
        return []
    res = []

    for i in range(len(digits)):
        dfs(i, digits, [], res)
    return res


def dfs(position, digits, comb, res):
    print(comb)
    print(position)
    if len(comb) == len(digits):
        res.append(''.join(comb[:]))
        return
    if position >= len(digits):
        # 这里是遇到了
        # comb = [d]
        # position = 2
        # 到了最后一位，同时comb没放满，但是dfs会执行到下一层，所以要手动停止了
        return
    candidates = phone[digits[position]]

    for i in candidates:
        temp = comb[:]
        temp.append(i)
        dfs(position+1, digits, temp, res)

letterCombinations("23")
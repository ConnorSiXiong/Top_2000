from typing import List


def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    res = []

    def dfs(start, sub_str):
        nonlocal res
        if start == len(digits):
            res.append(sub_str)
            return

        cur_dig = digits[start]
        characters = phone[cur_dig]
        # print(characters)

        for i in characters:
            temp_str = sub_str
            temp_str += i
            # print(temp_str)
            dfs(start+1, temp_str)

    dfs(0, '')

    return res

a = '234'
print(letterCombinations(a))

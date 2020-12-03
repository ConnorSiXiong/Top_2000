def decodeString1(s: str) -> str:
    stack = []
    cur_num = ''
    cur_str = ''
    for cur in s:
        if cur == '[':

            stack.append(cur_str)
            stack.append(int(cur_num))
            cur_num = ''
            cur_str = ''
        elif cur == ']':
            num = stack.pop()
            prev_str = stack.pop()
            cur_str = prev_str + cur_str * num
        # 23[ab]
        elif cur.isdigit():
            cur_num += cur
        # [ab]
        else:
            cur_str += cur

    return cur_str


s1 = "3[a]2[bc]"
a1 = "aaabcbc"

s2 = "3[a2[c]]"
a2 = "accaccacc"

s3 = "2[abc]3[cd]ef"
a3 = "abcabccdcdcdef"

s4 = "abc3[cd]xyz"
a4 = "abccdcdcdxyz"


def decodeString(s: str) -> str:
    num = ''
    string = ''
    stack = []

    for cur in s:
        if cur == '[':
            stack.append(int(num))
            stack.append(string)
            num = ''
            string = ''
        elif cur == ']':
            pre_s = stack.pop()
            pre_n = stack.pop()
            string = pre_s + string * pre_n
        elif cur.isdigit():
            num += cur
        else:
            string += cur

    return string

assert decodeString(s1) == a1
assert decodeString(s2) == a2
assert decodeString(s3) == a3
assert decodeString(s4) == a4

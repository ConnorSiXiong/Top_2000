def decodeString(s: str) -> str:
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


    return ''


s1 = "3[a]2[bc]"
a1 = "aaabcbc"

s2 = "3[a2[c]]"
a2 = "accaccacc"

s3 = "2[abc]3[cd]ef"
a3 = "abcabccdcdcdef"

s4 = "abc3[cd]xyz"
a4 = "abccdcdcdxyz"
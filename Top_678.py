def checkValidString(s: str) -> bool:
    if s is None:
        return True

    left = 0
    right = 0
    star = 0

    stack = []
    for current in s:
        if current == '(':
            if right != 0:
                right -= 1
            else:
                left += 1
                stack.append(current)
        elif current == '*':
            star += 1
            stack.append(current)
        else:
            if left == 0 and star == 0:
                return False
            if left != 0:
                left -= 1
                stack.reverse()
                stack.remove('(')
                stack.reverse()
            else:
                star -= 1
                stack.reverse()
                stack.remove('*')
                stack.reverse()
    print("left ", left)
    print("star ", star)
    print("right ", right)
    print("judge ", left <= star)

    if left == 0:
        return True
    elif left <= star:
        # 这一步要把所有的（ 去掉
        left2 = 0
        for i in stack:
            if i == '(':
                left2 += 1
            elif left2 != 0:
                left2 -= 1
        if left2:
            return False
        else:
            return True
    else:
        return False


a = "((((********))"
b = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
c = "((()))()(())(*()()())**(())()()()()((*()*))((*()*)"

print(checkValidString(a))

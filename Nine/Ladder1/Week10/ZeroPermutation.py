s = "001000"


#    0123456

def stringCount(s):
    # 超时间了
    res = 0
    for i in range(len(s) - 1):
        if s[i] == "1":
            continue
        j = i + 1

        # ----- 这部分代码导致了超时 ------
        while j < len(s) and s[j] == "0":
            j += 1
        # ----- 这部分代码导致了超时 ------

        if j < len(s) and s[j] == "1":
            res += (j - i)
        if j == len(s):
            res += (j - i)
    if s[-1] == "0":
        res += 1
    return res


# 优化代码
# 把 j 的初始化给优化了

s = "1111001100"


# s = "001000"
#    0123456

def stringCount2(s):
    # 在尾巴上加一个"1"，保证不会算漏掉最后一个 001000
    # 这种写法貌似比while循环两个值好
    s += "1"

    res = 0
    j = 1
    for i in range(len(s) - 1):
        if s[i] == "1":
            continue
        j = max(j, i + 1)
        while j < len(s) and s[j] == "0":
            j += 1
        # 上面的那个while直接让j走到头了
        # 所以不用进行其他的判断了，对比前面的方法
        res += (j - i)
    return res

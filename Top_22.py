# dfs + math

def generateParenthesis(n):
    if n == 1:
        return ["()"]

    res = []
    dfs(['('], 1, 0, res, n)
    print(res)
    return res


def dfs(comb, left, right, res, n):
    # 这样写是错的，而且错很远
    # 因为一直都指向内存的comb arr
    # 进入更深层的dfs后，最外层的一个pop不够

    # print后发现
    # 其实没pop到
    # 遇到非法组合后return，跳出直接回到pop()，只pop到当前非法的一次，没有和初始的append对应
    # 所以遇到这种问题，如果用数组写的话，每次有新的分支，一定要浅拷贝一下！

    if right > left:
        return
    if right == n and left == n:
        res.append(''.join(comb[:]))
        return
    print('inside', ''.join(comb[:]))
    if right < n:
        comb.append(')')
        dfs(comb, left, right + 1, res, n)
        print('before pop', ''.join(comb[:]))
        comb.pop()
        print('pop', ''.join(comb[:]))

    if left < n:
        comb.append('(')
        dfs(comb, left + 1, right, res, n)


def dfs2(comb, left, right, res, n):
    if right > left:
        return
    if right == n and left == n:
        res.append(''.join(comb[:]))
        return

    if right < n:
        temp_comb = comb[:]
        temp_comb.append(')')
        dfs(temp_comb, left, right + 1, res, n)
    if left < n:
        comb.append('(')
        dfs(comb, left + 1, right, res, n)


generateParenthesis(3)

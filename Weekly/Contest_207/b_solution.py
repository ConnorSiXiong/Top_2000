def maxUniqueSplit(s: str) -> int:

    haveBefore = set()
    res = 0

    def dfs(start):
        nonlocal res
        if start == len(s):
            res = max(res, len(haveBefore))
            return

        for i in range(start, len(s)):
            substr = s[start: i+1]
            if substr in haveBefore:
                continue
            haveBefore.add(substr)
            dfs(i + 1)
            haveBefore.remove(substr)
    dfs(0)
    return res


def maxUniqueSplit2(s: str) -> int:

    visited = set()
    res = 0

    def dfs(start):
        nonlocal res
        if start == len(s):
            # 当前组合遍历完了整个s
            # 且不重复组合都被存入了set里
            res = max(res, len(visited))
            return

        for i in range(start, len(s)):
            substr = s[start: i+1]
            print('substr', substr)
            if substr in visited:
                continue
            visited.add(substr)
            dfs(i + 1)
            print('out substr', substr)
            visited.remove(substr)

    dfs(0)

    return res


s = 'abc'

print(maxUniqueSplit2(s))



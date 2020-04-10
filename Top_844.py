def backspaceCompare(S: str, T: str) -> bool:
    return helper(S) == helper(T)


def helper(S: str) -> []:
    result = []
    for item in S:
        if item != '#':
            result.append(item)
        else:
            if len(result) != 0:
                result.pop()
    return result

S = "ab#c"
T = "ad#c"
print(backspaceCompare(S, T))
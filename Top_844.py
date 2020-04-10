def backspaceCompare(S: str, T: str) -> bool:
    return helper(S) == helper(T)


def helper(S: str) -> []:
    result = []
    for item in S:
        if item != '#':
            result.append(item)
        else:
            if len(result) != 0:
                # careful with empty list
                # S: a##c
                # T: #a#c
                result.pop()
    return result

S = "abc#d#"
T = "abc#"
print(backspaceCompare(S, T))
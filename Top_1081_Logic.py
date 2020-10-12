def removeDuplicateLetters(s: str):
    """

    Input: s = "bcabc"
    Output: "abc"


    Input: s = "cbacdcbc"
    Output: "acdb"
    """

    result = []
    visited = set()
    last = {c: i for i, c in enumerate(s)}

    for index, char in enumerate(s):
        if char not in visited:
            while result and char < result[-1] and index < last[result[-1]]:
                out = result.pop()
                visited.remove(out)

            result.append(char)
            visited.add(char)
    return result


aa = 'cbacdcbc'
print(removeDuplicateLetters(aa))

print('a' < 'b')

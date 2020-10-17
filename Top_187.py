from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:

    result = []
    visited_dict = {}

    for i in range(0, len(s) - 9):
        cut = s[i: i + 10]
        if cut not in visited_dict.keys():
            visited_dict[cut] = 1
        else:
            visited_dict[cut] = visited_dict.get(cut) + 1

    for k, v in visited_dict.items():
        if v >= 2:
            result.append(k)
    return result


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"
print(findRepeatedDnaSequences(s))

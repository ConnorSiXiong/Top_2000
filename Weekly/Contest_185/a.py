def reformat(s: str) -> str:
    if len(s) == 1:
        return s
    digits = "0123456789"
    box1 = []
    box2 = []
    for item in s:
        if item in digits:
            box1.append(item)
        else:
            box2.append(item)
    print(box1)
    print(box2)

    if len(box1) == 0 or len(box2) == 0:
        return ""
    result = ""
    if len(box1) == len(box2):
        for(a,b) in zip (box1, box2):
            current = a + b
            result += current
    elif len(box1) == len(box2) + 1:
        for (a, b) in zip(box1, box2):
            current = a + b
            result += current
        result += box1.pop()
    elif len(box1) == len(box2) - 1:
        for (a, b) in zip(box1, box2):
            current = b + a
            result += current
        result += box2.pop()
    return result

s = "abc12"
print(reformat(s))


def defangIPaddr(address: str) -> str:
    result = ''
    for i in address:
        if i != '.':
            result += i
        else:
            result += '[.]'
    return result


a = "1.1.1.1"

print(defangIPaddr(a))

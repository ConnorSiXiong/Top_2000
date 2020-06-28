def isPathCrossing(path: str) -> bool:
    counter = {}
    check_turn = []
    for index, direction in enumerate(path):
        if direction not in counter:
            counter[direction] = 1
            check_turn.append(direction)
        else:
            counter[direction] += 1

    if len(check_turn) == 3 or len(check_turn) == 1:
        return False
    if len(check_turn) == 2:
        if 'N' in check_turn and 'S' not in check_turn:
            return False
        elif 'S' in check_turn and 'N' not in check_turn:
            return False
        elif 'E' in check_turn and 'W' not in check_turn:
            return False
        elif 'W' in check_turn and 'E' not in check_turn:
            return False
        else:
            return True

    num_n = counter['N']
    num_s = counter['S']
    num_e = counter['E']
    num_w = counter['W']

    if check_turn[0] == 'N':
        if num_s >= num_n:
            check_turn.remove('S')
            check_turn.remove('N')
            if check_turn[0] == 'W':
                if num_e >= num_w:
                    return True
            else:
                if num_e <= num_w:
                    return True
    elif check_turn[0] == 'S':
        if num_n >= num_s:
            check_turn.remove('S')
            check_turn.remove('N')
            if check_turn[0] == 'W':
                if num_e >= num_w:
                    return True
            else:
                if num_e <= num_w:
                    return True
    elif check_turn[0] == 'W':
        if num_e >= num_w:
            check_turn.remove('E')
            check_turn.remove('W')
            if check_turn[0] == 'N':
                if num_s >= num_n:
                    return True
            else:
                if num_s <= num_n:
                    return True
    elif check_turn[0] == 'E':
        if num_w >= num_e:
            check_turn.remove('E')
            check_turn.remove('W')
            if check_turn[0] == 'N':
                if num_s >= num_n:
                    return True
            else:
                if num_s <= num_n:
                    return True
    return False


def isPathCrossing2(path: str) -> bool:
    """
        N
     W     E
        S
    """
    x = 0
    y = 0

    trace = set()
    trace.add((0,0))
    for i in path:
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'W':
            x -= 1
        else:
            x += 1
        current = (x, y)
        if current in trace:
            return True
        else:
            trace.add(current)
    return False


print(isPathCrossing2("NESWW"))

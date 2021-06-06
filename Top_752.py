import collections

POSITION = [0, 1, 2, 3]


def openLock(deadends, target):
    # 这个开锁题就是注意一下反向走
    # 一个位置的数字可以 +1 也可以 -1

    if "0000" in deadends:
        return -1
    q = collections.deque([])
    q.append(["0000", 0])
    visited = set("0000")  # 这个地方写掉了
    for i in deadends:
        visited.add(i)
    while q:
        cur_number, step = q.popleft()

        if isUnlock(cur_number, target):
            return step

        for pos in POSITION:
            for direction in (-1, 1):
                next_number = getNextNumber(cur_number, pos, direction)
                if next_number in visited:
                    continue
                q.append([next_number, step + 1])
                visited.add(next_number)
    return -1


def isUnlock(cur, target):
    return True if cur == target else False


def addOne(digit):
    digit = int(digit)
    if digit == 9:
        return "0"
    else:
        return str(digit + 1)


def minusOne(digit):
    digit = int(digit)
    if digit == 0:
        return "9"
    else:
        return str(digit - 1)


def getNextNumber(cur_number, position, direction):
    cur_number = list(cur_number)
    cur_digit = cur_number[position]
    if direction == 1:
        next_digit = addOne(cur_digit)
        cur_number[position] = next_digit

        return "".join(cur_number)
    else:
        next_digit = minusOne(cur_digit)
        cur_number[position] = next_digit
        return "".join(cur_number)


def neighbors(node):
    for i in range(4):
        x = int(node[i])
        for d in (-1, 1):
            y = (x + d) % 10
            yield node[:i] + str(y) + node[i + 1:]


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print(openLock(deadends, target))

def leftMostColumnWithOne(matrix) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    result = -1
    running = True

    x = 0
    y = cols - 1

    while running:

        cur = matrix[x][y]

        if cur == 0:
            if x != rows - 1:
                x += 1
            elif x == rows - 1:
                y -= 1
        elif cur == 1:
            result = y
            if y >= 0:
                y -= 1

        if y == -1:
            running = False

    return result


mat = [[0,0,0,1],
       [0,0,0,1],
       [0,0,1,1],
       [0,0,0,0]
       ]
print(leftMostColumnWithOne(mat))
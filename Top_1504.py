import sys


def counter_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])

    width_matrix = [[0] * cols for _ in range(rows)]
    print(width_matrix)
    # from left to right
    for i in range(rows):
        for j in reversed(range(cols)):

            if mat[i][j] == 1:
                # 边界
                if j != cols - 1:
                    width_matrix[i][j] = 1 + width_matrix[i][j + 1]
                else:
                    width_matrix[i][j] = 1
    print(width_matrix)
    result = 0
    for i in range(rows):
        for j in range(cols):
            width = sys.maxsize
            for row in range(i, rows):
                width = min(width, width_matrix[row][j])
                result += width
    print(result)
    return result


def submat(mat):
    m = len(mat)
    n = len(mat[0])

    one_counts = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n - 1, -1, -1):
            if mat[i][j] == 1:
                one_counts[i][j] += 1 + (one_counts[i][j + 1] if j < n - 1 else 0)

    ans = 0
    box = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                min_w = sys.maxsize
                for k in range(i, m):
                    min_w = min(min_w, one_counts[k][j])
                    # print('k', k, 'j', j)

                    # min_w = one_counts[k][j]
                    # print(min_w)
                    box.append(min_w)
                    ans += min_w
    print(ans)
    return ans


a = [[0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 1, 1, 0]]
# submat(a)

b = [1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 2, 1]
c = [1, 2, 2, 1, 0, 0, 2, 2, 1, 1, 2, 1]

counter_matrix(a)

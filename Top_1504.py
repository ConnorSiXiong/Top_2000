from typing import List


def num_mat(mat: List[List[int]]) -> int:
    """
    Q3

    这是一个java根据每一row的解法，但是可解释性不强
    当处理完row，处理col的时候，没有办法解释面积>1的矩形是怎么计数的（就是+1)

    int m = matrix.length, n = matrix[0].length, res = 0;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                // matrix stores num of consecutive ones from matrix[i][j] first zero on its right
                matrix[i][j] = matrix[i][j] == 0 ? 0 : matrix[i][j] + matrix[i][j + 1];
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int min = matrix[i][j];
                res += min;
                for (int k = i + 1; k < m; k++) {
                    if (matrix[k][j] == 0) break;
                    min = Math.min(min, matrix[k][j]); # 就是这个地方
                    res += min;
                }
            }
        }
        return res;
    """
    rows = len(mat)
    cols = len(mat[0])
    res = 0



    return res


def one_row(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    counter = 0
    accumulated_rect = 0
    for i in arr:
        if i == 1:
            accumulated_rect = accumulated_rect + 1  # 这个地方没看懂，为什么要累加
        else:
            accumulated_rect = 0
        counter += accumulated_rect
    return counter


def numSubmat2(self, mat: List[List[int]]) -> int:
    rows = len(mat)
    cols = len(mat[0])
    a = mat
    ret = 0
    f = [[0] * cols for _ in range(rows)]

    allonecols = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if a[i][j] == 1:
                allonecols[i][j] = (allonecols[i - 1][j] if i > 0 else 0) + 1
    # print("allonecols", allonecols)
    for k in range(1, rows + 1):
        for i in range(rows):
            for j in range(cols):
                if allonecols[i][j] >= k:
                    c = f[i][j] = (f[i][j - 1] if j > 0 else 0) + 1
                    ret += c
                else:
                    f[i][j] = 0
        # print("f", f)
    return ret
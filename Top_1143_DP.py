import numpy


def longestCommonSubsequence(text1: str, text2: str) -> int:

    a = len(text1)
    b = len(text2)

    dp = numpy.zeros((a+1, b+1), dtype=numpy.int)

    for i in range(a):
        for j in range(b):
            # 'c' means 'char'
            c1 = text1[i]
            c2 = text2[j]

            if c1 == c2:
                # 两个字符一样
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(dp)
    return dp[a][b]

t1 = 'abcde'
t2 = 'ace'
longestCommonSubsequence(t1,t2)




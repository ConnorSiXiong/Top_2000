import numpy as np


def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)

    dp = np.zeros((len(s1) + 1, len(s2) + 1), bool)
    dp[0, 0] = True

    for i in range(1, len(s1) + 1):
        dp[i, 0] = dp[i - 1, 0] and s1[i - 1] == s3[i - 1]
    for i in range(1, len(s2) + 1):
        dp[0, i] = dp[0, i - 1] and s2[i - 1] == s3[i - 1]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i, j] = (dp[i - 1, j] and s1[i - 1] == s3[i + j - 1]) or (dp[i, j - 1] and s2[j - 1] == s3[i + j - 1])
    print(dp)
    return dp[-1, -1]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))

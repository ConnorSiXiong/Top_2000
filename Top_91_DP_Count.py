class Solution:
    def numDecodings(self, s: str) -> int:
        """
        状态转移方程的理解是：
        dp加出来的一维是存放结果用的

        站在当前位，计算一个数字的所有，或者两位数组组合的所有

        """
        if len(s) == 1:
            if s[0] == "0":
                return 0
            return 1

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if 1 <= int(s[i - 1:i]) <= 9:
                # 这里dp[i]是当前位的可能组合数
                # dp[i-1]的意思就是，把当前位的数字取出来s[i-1:i],前面那可能组合方案数就是dp[i-1]
                dp[i] += dp[i - 1]

            if i >= 2:
                if 10 <= int(s[i - 2:i]) <= 26:
                    # 这里dp[i]是当前位的可能组合数
                    # dp[i-2]的意思就是，把当前2位的数字取出来s[i-2:i],前面的可能组合方案数就是dp[i-2]
                    dp[i] += dp[i - 2]
        return dp[-1]

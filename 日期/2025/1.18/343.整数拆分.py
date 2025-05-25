#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(dp[i - j]*j, (i-j)*j))
        return dp[n]
# @lc code=end


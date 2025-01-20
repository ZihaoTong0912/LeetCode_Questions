#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 3:
            return n
        dp = [n] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        number = [1]
        for i in range(4,n+1):
            if (int(i**0.5))**2 ==i:
                dp[i] = 1
                number.append(i)
            for j in number:
                dp[i] = min(dp[i], dp[i-j] +1)
        return dp[n]


# @lc code=end


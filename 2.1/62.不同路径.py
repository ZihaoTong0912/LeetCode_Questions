#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def fun(a,b):
            if (a,b) in memo:
                return memo[(a,b)]
            if a == m and b == n:
                return 1
            if a == m:
                return fun(a,b+1)
            if b == n:
                return fun(a+1,b)

            memo[(a,b)] = fun(a+1,b)+fun(a,b+1)
            return memo[(a,b)]
        return fun(1,1)
# @lc code=end


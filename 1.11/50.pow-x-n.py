#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fun(x,n):
            if n == 0:
                return 1
            half = fun(x, n//2)
            if n > 0:
                if n % 2 == 0:
                    return half*half
                else:
                    return half*half*x
        if n < 0:
            x = 1/x
            n = -n
        return fun(x,n)
# @lc code=end


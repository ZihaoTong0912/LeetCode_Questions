#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
# 这道题和 和最大子数组是一个道理
# 唯一的区别就是也要记录最小值也就是负数值，
# 来避免错过负数情况下的最大子数组。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f_max = [0] * n
        f_min = [0] * n
        f_max[0] = f_min[0] = nums[0]
        for i in range(1,n):
            x = nums[i]
            f_max[i] = max(f_max[i-1]*x,f_min[i-1]*x, x)
            f_min[i] = min(f_max[i-1]*x,f_min[i-1]*x, x)
        return max(f_max)
# @lc code=end


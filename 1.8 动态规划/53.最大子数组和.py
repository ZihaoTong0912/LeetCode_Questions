#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = len(nums) * [nums[0]]
        for i in range(1, len(nums)):
            if dp [i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
        return max(dp)

# @lc code=end


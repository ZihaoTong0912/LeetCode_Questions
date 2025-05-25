#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        tmp = 1
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            tmp *= nums[j+1]
            output[j] *= tmp
        return output

# @lc code=end


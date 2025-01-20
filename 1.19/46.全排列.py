#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def fun(x):
            if x == len(nums) -1:
                output.append(list(nums))
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                fun(x+1)
                nums[i],nums[x] = nums[x], nums[i]

        fun(0)
        return output
# @lc code=end


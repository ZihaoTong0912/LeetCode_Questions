#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            output = output +[[i] + num for num in output]
        return output

# @lc code=end


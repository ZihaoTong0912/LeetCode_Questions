#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(x):
            if x == len(nums)-1:
                output.append(list(nums))
                return 
            repeat = set()
            for i in range(x,len(nums)):
                if nums[i] in repeat:
                    continue
                repeat.add(nums[i])
                nums[x], nums[i] = nums[i], nums[x]
                dfs(x+1)
                nums[x], nums[i] = nums[i], nums[x]
        dfs(0)
        return output
# @lc code=end


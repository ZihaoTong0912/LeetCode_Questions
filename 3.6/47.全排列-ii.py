#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
# 这里求的全排列 依赖的是回溯的做法，
# 通过一个for循环来确定每一位数的位置，
# 当到达目标长度时，在output中添加该排列。
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


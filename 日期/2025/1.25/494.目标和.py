#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p 就是留着当正数的数
        # s-p就是当负数的数的正数和
        # 所以 target 就是 p - (s-p)
        # 也就是说 2p-s = target
        # p = (target+s)/2
        # 题目也就变成了 在nums里面选数使得和为p.
        p = target+sum(nums)
        if p % 2 == 1 or p < 0:
            return 0
        p = p // 2
        @cache
        def dfs(i,c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i-1, c)
            return dfs(i-1,c) + dfs(i-1, c-nums[i])
        return dfs(len(nums)-1, p)

# @lc code=end


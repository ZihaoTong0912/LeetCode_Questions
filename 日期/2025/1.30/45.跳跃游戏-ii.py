#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
# 这里用的是记忆化递归 时间复杂度为n^2。
# 该方法时间复杂度太高，因此可能会导致超时
# 所以更适合使用贪心算法

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def fun(i):
            pre = float('inf')
            if i >= n-1:
                return 0
            if nums[i] == 0:
                return inf
            for j in range(1,nums[i]+1):
                output = fun(i+j) +1
                pre = min(output, pre)
            return pre
        return fun(0)
# @lc code=end


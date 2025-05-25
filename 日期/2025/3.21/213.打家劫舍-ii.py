#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start

# 思路就是首先从上一题能得知 前N+1的 房间的最大值
# 其实就是 N的最大值 和N-1的最大值加上当前房间的值
# 这两个当中的一个 所以就可以得出递推式
# total_max[n+1] = max(total_max[n], total_max[n-1] + nums[n+1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def fun(nums):
            cur = 0
            pre = 0
            for num in nums:
                cur, pre = max(pre+num, cur), cur
            return cur
        return max(fun(nums[1:]), fun(nums[:-1]))

# @lc code=end


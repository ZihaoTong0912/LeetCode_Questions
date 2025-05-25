#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# 这道题通过筛选了一些不可能的结果来避免了重复计算，从而降低了暴力解法的
# 时间复杂度。首先通过排序，然后当nums[k]大于0时，意味着三数的和一定大于0。
# 而且通过筛选来跳过重复的 nums[k], nums[i], nums[j]。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for k in range(n-2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = n-1
            while i < j:
                s = nums[k]+nums[i]+nums[j]
                if s < 0:
                    i += 1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    output.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return output
# @lc code=end


#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        tmp = nums[n-k:]
        numscopy=nums[:]
        for i in range(len(nums) - k):
            nums[i+k] = numscopy[i]
        nums[:k] = tmp 
        
# @lc code=end


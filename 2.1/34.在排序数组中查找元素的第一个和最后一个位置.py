#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(target):
            i = 0
            j = len(nums)-1
            while i <= j:
                m = (i+j)//2
                if nums[m] <= target:
                    i = m + 1
                else:
                    j = m-1
            return i
        if search(target-1) <= search(target)-1:
            return [search(target-1),search(target)-1]
        else:
            return [-1,-1]
# @lc code=end


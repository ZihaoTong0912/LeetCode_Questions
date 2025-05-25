#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        def pivot(nums, l, r):
            ra = random.randrange(l, r + 1)
            nums[l], nums[ra] = nums[ra], nums[l]
            i,j = l, r
            while i < j:
                while i < j and nums[j] >= nums[l]:
                    j -= 1
                while i < j and nums[i] <= nums[l]:
                    i += 1
                nums[j],nums[i] = nums[i],nums[j]
            nums[l],nums[i] = nums[i], nums[l]
            return i
        def quicksort(nums,l,r):
            while l < r:
                i = pivot(nums, l, r)
                if i - 1 < r - i:
                    quicksort(nums,l, i-1)
                    l = i + 1
                else:
                    quicksort(nums,i+1, r)
                    r = i - 1
        quicksort(nums,l,r)
        return nums

# @lc code=end


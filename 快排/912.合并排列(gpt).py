#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            
            return merge(left_half, right_half)
        def merge(left,right):
            i = 0
            j = 0
            output = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    j += 1
            output.extend(left[i:])
            output.extend(right[j:])
            return output
        return merge_sort(nums)

# @lc code=end


#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
# 归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            merge_sort(nums, l, m)
            merge_sort(nums, m + 1, r)

            tmp = nums[l:r + 1]       # 暂存需合并区间元素
            i, j = 0, m - l + 1       # 两指针分别指向左/右子数组的首个元素
            for k in range(l, r + 1): # 遍历合并左/右子数组
                if i == m - l + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r - l + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
        l= 0
        r = len(nums)-1
        merge_sort(nums,l, r)
        return nums

# @lc code=end


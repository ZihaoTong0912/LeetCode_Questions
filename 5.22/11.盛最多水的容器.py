#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start

# 这题主要思路是根据 当我们计算面积时， 若是缩进长线
# 则面积只会下降或者不变 若是缩进短线 面积有可能会增长
# 因此使用双指针，每次只缩进短线并寻找最大面积就能保证
# 找到最大面积
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        output = 0
        while i < j:
            if height[i] < height[j]:
                output = max(output, (j-i)*height[i])
                i += 1
            else:
                output = max(output, (j-i)*height[j])
                j -= 1
        return output

# @lc code=end


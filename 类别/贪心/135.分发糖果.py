#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
# 题目的思路是 首先给每个孩子一颗糖 若要满足
# 相邻的学生获得更高的糖果 则等价于
# 当右边的学生rating大于左边的时候 
# 右边的学生获得的糖比左边多
# 当左边的学生rating 大于右边的时候
# 左边的学生获得糖比右边多
# 因此 先从左往右遍历， 
# 使得 left数组满足 右边的学生糖比左边多
# 再从右往左遍历 
# 使得 right数组满足左边的学生糖比右边多
# 接下来只要取两数组中的最大值 来计算总数
# 就可以保证 同时满足左和右两种条件了。
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] =left[i-1] +  1
        count = left[-1]
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1]+1
            count += max(right[j], left[j])
        return count
# @lc code=end


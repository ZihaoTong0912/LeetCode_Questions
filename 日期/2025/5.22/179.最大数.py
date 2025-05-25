#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start

# 通过写定一个新的sort rule, 可以用sort函数来排序列表
# 思路是因为当字符串x+y < y+x 时 说明x > y
# 若 x+y < y + x 则说明x < y
# sort_rule 中的 -1, 0, 1 是在cmp_to_key 中是必须的
# 代表了 小于 等于 和大于
# cmp_to_key 需要从functools 里面import
# 通过这样的sort rule重新排序后 直接拼接字符串就行了

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_rule(x,y):
            a,b = x+y, y+x
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0
        strs = [str(num) for num in nums]
        strs.sort(key=cmp_to_key(sort_rule))
        if strs[0] == '0':
            return '0'
        return ''.join(strs)
# @lc code=end


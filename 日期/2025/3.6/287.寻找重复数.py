#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = ''
            else:
                return i
# @lc code=end


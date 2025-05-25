#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            s = s[1:] + s[:1]
            if s == goal:
                return True
            
        return False
# @lc code=end


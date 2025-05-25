#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        output_value = 0
        while j <= len(s):
            substr = s[i:j]
            if len(set(substr)) == len(substr):
                j += 1
                output_value = max(output_value, len(substr))
            else:
                i += 1
        return output_value
# @lc code=end


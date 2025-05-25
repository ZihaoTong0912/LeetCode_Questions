#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        symbol_dict = {'[':']', '(':')', '{':'}','.': '.'}
        stack = ['.']
        for i in s:
            if i in symbol_dict:
                stack.append(i)
            else:
                deleted = stack.pop()
                if symbol_dict[deleted] != i:
                    return False
        return len(stack) == 1

                
# @lc code=end


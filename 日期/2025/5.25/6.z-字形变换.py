#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start

# 本体思路是 将题目中的所谓Z字变换 转换为每个字符所在的行数
# 例如numRows = 4时 其实字符规律就是:
# 1234321234321
# 因此通过i来记录每个字母的行数 然后用flag控制
# i在1234321这个规律中 增大和减小 
# 然后把每行字符串加起来就可以了。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        list_rows = ['' for _ in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            list_rows[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return ''.join(list_rows)
# @lc code=end


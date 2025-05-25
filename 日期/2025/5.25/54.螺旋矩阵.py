#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start

# 思路很简单 其实就是把每种情况的for循环写出来，都放在一个while循环里。
# 当不满足条件时，比如top>bot,亦或是l > r,这类情况
# 就直接break掉while循环就可以了。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0])-1
        top = 0
        bot = len(matrix)-1
        output = []
        while True:
            for i in range(l,r+1):
                output.append(matrix[top][i])
            top += 1
            if top > bot:
                break
            for i in range(top, bot+1):
                output.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                output.append(matrix[bot][i])
            bot -= 1
            if top > bot:
                break 
            for i in range(bot, top-1, -1):
                output.append(matrix[i][l])
            l += 1
            if l > r:
                break 
        return output
        
# @lc code=end


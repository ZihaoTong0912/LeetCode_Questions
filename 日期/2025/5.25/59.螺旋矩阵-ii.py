#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start

# 跟螺旋矩阵 I 思路基本一样 
# 同样是写一个while 循环嵌套多个for循环来满足条件 
# 但这次的break条件是当写入的数字大于n的平方的时候。
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        output = [[0 for i in range(n)] for i in range(n)]
        l = 0
        r = n-1
        top = 0
        bot = n-1
        while True:
            for i in range(l,r+1):
                output[top][i] = num
                num += 1
            top += 1
            if num > n**2:
                break
            for i in range(top, bot+1):
                output[i][r] = num 
                num += 1
            r -= 1
            if num > n**2:
                break
            for i in range(r,l-1, -1):
                output[bot][i] = num 
                num += 1
            bot -= 1
            if num > n**2:
                break
            for i in range(bot,top-1, -1):
                output[i][l] = num
                num += 1
            l += 1
            if num > n**2:
                break

        return output
# @lc code=end


#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [False]*len(matrix)
        col = [False]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                   row[i],col[j] = True, True
            

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        
# @lc code=end


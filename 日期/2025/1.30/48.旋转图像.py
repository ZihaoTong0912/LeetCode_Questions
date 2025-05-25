#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        deque = collections.deque()
        for i in range(n):
            for j in range(n):
                deque.append(matrix[i][j])
        
        for i in range(n-1,-1,-1):
            for j in range(n):
                matrix[j][i] = deque.popleft()
        
        
# @lc code=end


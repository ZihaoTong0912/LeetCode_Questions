#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def fun(i, j , k):
            if not 0 <= i <= len(board)-1 or not 0<= j <= len(board[0])-1 or board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            board[i][j] = ''
            res = fun(i+1,j,k+1) or fun(i,j+1,k+1) or fun(i-1,j,k+1) or fun(i,j-1,k+1)
            board[i][j] = word[k]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if fun(i,j,0):
                    return True 
        return False


# @lc code=end


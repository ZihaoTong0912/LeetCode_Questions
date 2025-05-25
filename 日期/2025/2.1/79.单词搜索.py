#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start

# 这题的思路是 深度优先搜索 并搭配剪枝 也就是说 当一条路径走不通时 果断放弃这条路径
# 从终止条件入手，若搜索超过矩阵外 亦或是不满足当前的k 直接返回False
# 然后通过回溯，来防止遍历到已经遍历过的字母来防止死循环
# 最后通过两个for循环来将每个字母作为起点 然后返回 True or False.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            if not 0 <= i < len(board) or not 0 <= j <len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res =  dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i, j+1, k+1)
            board[i][j] = word[k]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True 
        return False
# @lc code=end


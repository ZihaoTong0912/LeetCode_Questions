#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            output = [[1], [1,1]]
            for j in range(3, numRows+1):
                new_list = j * [1]
                for i in range(1, len(output[-1])):
                    new_list[i] = output[-1][i-1] + output[-1][i]
                output.append(new_list)
            return output

# @lc code=end


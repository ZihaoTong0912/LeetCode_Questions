#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        output = []
        while j < len(prices):
            if min(prices[i], prices[j]) == prices[i]:
                output.append(prices[j] - prices[i])
            else:
                i = j
            j += 1
        if len(output) == 0:
            return 0
        return max(output)

# @lc code=end


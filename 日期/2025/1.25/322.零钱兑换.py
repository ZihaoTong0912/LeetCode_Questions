#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, amount):
            if i < 0:
                return 0 if amount == 0 else inf
            if amount < coins[i]:
                return dfs(i - 1, amount)
            return min(dfs(i - 1, amount), dfs(i, amount - coins[i]) + 1)

        output = dfs(len(coins) - 1, amount)
        return output if output < inf else -1
# @lc code=end


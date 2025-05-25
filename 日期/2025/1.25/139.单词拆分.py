#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len,(wordDict)))
        words = set(wordDict)
        @cache
        def dfs(i):
            if i == 0:
                return True
            for j in range(max(0,i-max_len),i):
                if s[j:i] in words and dfs(j):
                    return True
            return False
        return dfs(len(s))

# @lc code=end


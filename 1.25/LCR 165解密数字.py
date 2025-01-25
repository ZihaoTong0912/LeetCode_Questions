class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        ciphertext = str(ciphertext)
        memo = [-1]* (len(ciphertext)+1)
        def dfs(n):
            if n < 2:
                return 1
            if memo[n] != -1 and n >= 0:
                return memo[n]
            if '10' <= ciphertext[n-2:n] <= '25':
                val = dfs(n-1) + dfs(n-2) 
                memo[n] = val
                return val
            else:
                val = dfs(n-1)
                memo[n] = val 
                return val
        return dfs(len(ciphertext))
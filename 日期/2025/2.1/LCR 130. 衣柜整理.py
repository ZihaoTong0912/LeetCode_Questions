# 这道题中digit是位数和的计算 我们通过计算位数和，以及一个用来记录已访问过的
# 书柜的字典，来创建终止条件。最后我们从0出发，然后找到所有访问的到的书柜。
# 在写这类题时，总是会弄错边界条件，像这道题就弄错了m和n，下次要注意。
class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        def digit(x):
            output = 0
            for i in str(x):
                output += int(i)
            return output
        dict1 = {}
        def dfs(i,j,cnt):
            if digit(i) + digit(j) > cnt or i >= m or j >= n or (i,j) in dict1:
                return 0
            dict1[(i,j)] = ''
            return dfs(i+1,j,cnt)+1+dfs(i,j+1,cnt)
        return dfs(0,0,cnt)
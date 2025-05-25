class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 思路是通过一个hashtable来记录坐标 
        # 如果同样的字母再次出现 就更新左指针
        # max的目的是为了保证指针只会往右跳
        # 比如aabb的情况 就会报错
        output = 0
        dict1 = {}
        i = -1
        for j in range(len(s)):
            if s[j] in dict1:
                i = max(i,dict1[s[j]])
            dict1[s[j]] = j
            output = max(output, j-i)
        return output

            
class Solution:
    def reverseWords(self, s: str) -> str:
        # 思路是双指针检测单个单词 然后置入list
        # 之后再用.join 来整合
        s = s.strip()
        output_list = []
        left = len(s)-1
        right = len(s)
        while left >= 0:
            while left >= 0 and s[left] == ' ':
                left -= 1
            right = left + 1
            while left >= 0 and s[left] != ' ':
                left -= 1
            
            output_list.append(s[left+1:right])

        return ' '.join(output_list)
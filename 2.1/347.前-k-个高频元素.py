#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        list1 = []
        for i in count.values():
            list1.append(i)
        list1.sort()
        list1 = list1[len(list1)-k:]
        output = []
        for i in count.keys():
            if count[i] in list1:
                output.append(i)
        return output
            
# @lc code=end


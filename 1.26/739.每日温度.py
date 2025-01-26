#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
# 思路在于 用单调栈（递减） 每次遍历是 看看i是否比栈内的最小值大 如果是
# 则出栈 再看i是否比栈内的最小值 大 依次检查， 如果没有了 则说明该元素是
# 最小的元素 入栈。
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        deque = collections.deque()
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while deque and temperatures[i] > temperatures[deque[-1]]:
                index = deque.pop()
                output[index] = i-index
            deque.append(i)

        return output



# @lc code=end


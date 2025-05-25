#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#

# @lc code=start

# 本题思路 首先是
#排序块定义：
#排序块 充分条件： 设此块中最大数字为 head , 若此块后面的所有数字都 >=head ，则此块为排序块。
#排序块 最短长度为 1，即单个元素可以独立看作一个排序块。

# 因此可以遍历整个数组 并通过栈来存储head。
# 若当前num 小于栈中的最大的head, 则检查当前num是否也小于栈中的其他head
# 若是，依次排除这些head(也可以解释为合并这些head)
# 若当前num 大于栈中的最大的head, 则直接将num 加入head。 
# 是一种单调栈的运用。(我认为)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        return len(stack)
# @lc code=end


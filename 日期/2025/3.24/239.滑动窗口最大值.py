#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start

### 这题思路是 确保滑动窗口单调递减 也就是说 最左边的永远是最大值 
### 因此每次迭代都只用在output列表中加入最左边的最大值

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = []
        deque = collections.deque()
        for i, j in zip(range(1-k, n + 1 - k), range(n)):

            # 当最大值需要被弹出时 弹出最大值
            if i > 0 and nums[i-1] == deque[0]:
                deque.popleft()

            # 通过每次加入第j个数前 删除比第j个数小的值来保证单调递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            
            # 在双端列表中加入第j各数
            deque.append(nums[j])

            # 如果i大于0 就开始在输出列表中加入最大值 
            if i >= 0:
                output.append(deque[0])
        return output
# @lc code=end


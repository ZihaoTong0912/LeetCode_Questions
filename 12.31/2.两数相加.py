#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        j = 0
        sum1 = 0
        sum2 = 0
        while l1:
            sum1 += (10**(i))*l1.val
            l1 = l1.next
            i += 1
        while l2:
            sum2 += (10**(j))*l2.val
            l2 = l2.next
            j += 1
        sum_total = sum1 + sum2 
        d1 = deque()
        for k in str(sum_total):
            d1.append(int(k))
        head = ListNode(d1.pop())
        cur = head
        while len(d1) > 0:
            cur_next = ListNode(d1.pop())
            cur.next = cur_next
            cur = cur_next
        return head
# @lc code=end


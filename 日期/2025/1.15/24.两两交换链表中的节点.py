#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def fun(cur):
            if not cur or not cur.next:
                return cur
            newHead = cur.next
            cur.next = fun(newHead.next)
            newHead.next = cur
            return newHead 
        return fun(head)
            
            
# @lc code=end


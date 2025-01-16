#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        if length == 1:
            return 
        if length == n:
            return head.next
        cur = head
        for i in range(length - n-1):
            cur = cur.next
        tmp = cur.next 
        cur.next = tmp.next 
        tmp.next = None
        return head
# @lc code=end


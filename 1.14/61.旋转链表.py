#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        length = 1
        tmp = head 
        while tmp.next:
            tmp = tmp.next 
            length+= 1
        if k >= length:
            k = k % length
        if k == 0:
            return head
        tmp = head
        while tmp:
            last_node = tmp 
            tmp = tmp.next
        last_node.next = head
        tmp = head
        len_new_head = length - k
        for i in range(len_new_head-1):
            tmp = tmp.next
        new_head = tmp.next
        tmp.next = None
        return new_head
# @lc code=end


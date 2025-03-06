#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 思路: 遍历一遍链表 将大于和小于x的数分别存于两个不同的链表 
        # 然后再把他们连起来
        smaller_head = ListNode(0)
        large_head = ListNode(0)
        small = smaller_head
        large = large_head
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next 
            head = head.next
        small.next = large_head.next
        large.next = None 
        return smaller_head.next

# @lc code=end


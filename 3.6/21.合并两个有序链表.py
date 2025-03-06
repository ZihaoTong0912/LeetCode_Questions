#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return []
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        tmp = head
        while list1 or list2:
            if list1 and not list2:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
            elif list2 and not list1:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
            elif list1 and list2:
                if list1.val > list2.val:
                    tmp.next = list2
                    tmp = tmp.next
                    list2 = list2.next
                else:
                    tmp.next = list1
                    tmp = tmp.next
                    list1 = list1.next
        return head

# @lc code=end


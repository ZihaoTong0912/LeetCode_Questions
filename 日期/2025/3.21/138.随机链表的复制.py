#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        dict1 = {}
        while node:
            dict1[node] = Node(node.val)
            node = node.next 
        node = head
        while node:
            dict1[node].next = dict1.get(node.next)
            dict1[node].random = dict1.get(node.random)
            node = node.next
        return dict1[head]
        
# @lc code=end


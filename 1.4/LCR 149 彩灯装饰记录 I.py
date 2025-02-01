# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 这道题采用一个双端列表来存储数字，通过先验证条件if poped.left 再验证
# if poped.right来确保是从左到右记录value，并按照先进先出的队列方式。
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            poped = queue.popleft()
            output.append(poped.val)
            if poped.left:
                queue.append(poped.left)
            if poped.right:
                queue.append(poped.right)
        return output
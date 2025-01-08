# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
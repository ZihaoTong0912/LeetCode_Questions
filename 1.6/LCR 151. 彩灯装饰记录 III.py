# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        output = []
        queue.append(root)
        i = 1
        while queue:
            temp = collections.deque()
            for _ in range(len(queue)):
                poped = queue.popleft()
                if i % 2 == 1:
                    temp.append(poped.val)
                else:
                    temp.appendleft(poped.val)
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
            i += 1
            output.append(list(temp))
        return output
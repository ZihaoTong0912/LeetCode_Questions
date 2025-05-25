# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 这道题和上一道题很像，唯一的区别就是要通过一个list来存储
# 每一层。所以区别就是这里使用了for 循环来区分每一层
# 的遍历。
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                temp.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            output.append(temp)
        return output
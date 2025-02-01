# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 这道题要求的是彩灯装饰记录2的变体，也就是第一层用左到右的顺序，
# 第二层用右到左的顺序。这里的想法是通过i来记录单双数层数，
# 每次还是从左到右记录进deque，使用辅助栈temp来记录value，
# 使用append来保证是从左到右的记录，用appendleft来确定是从右到左的记录
# 利用了双端队列的特性 也就是既可以堆叠也可以放在最前面。
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
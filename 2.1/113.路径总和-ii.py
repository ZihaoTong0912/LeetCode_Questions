#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 这题的思路其实就是用回溯的方法，然后前序遍历（根-左子树-右字数的顺序）来检索每条
# 路径。 path.append和path.pop使用了回溯的方法来试探和撤销。在退出当前路径时会依次
# 撤销之前加入的value。还有个细节就是list(path)，这样会创造一个，以防止之后对path的
# 改动对之前已经录入的路径产生影响。
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        path = []
        def rec(root,target):
            if not root:
                return 
            target -= root.val
            path.append(root.val)
            if target == 0 and not root.left and not root.right:
                output.append(list(path))
            rec(root.left,target)
            rec(root.right,target)
            path.pop()
        rec(root,targetSum)
        return output
# @lc code=end


#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def fun(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return fun(L.left, R.right) and fun(L.right,R.left)
        return not root or fun(root.left, root.right)
# @lc code=end


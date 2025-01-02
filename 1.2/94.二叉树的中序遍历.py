#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursionf(root, output_list = None):
            if output_list is None:
                output_list = []
            if root:
                recursionf(root.left,output_list)
                output_list.append(root.val)
                recursionf(root.right, output_list)
            return output_list
        output = recursionf(root)
        return output
            
            
# @lc code=end


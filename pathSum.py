'''
https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum

        fill = targetSum - root.val
        return self.hasPathSum(root.right, fill) or self.hasPathSum(root.left, fill)


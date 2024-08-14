'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150

Recursive DFS 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_number: int) -> int:
            if not node:
                return 0
            
            # Update the current number formed so far
            current_number = current_number * 10 + node.val
            
            # If we're at a leaf node, return the current number
            if not node.left and not node.right:
                return current_number
            
            # Recur for both left and right subtrees and sum up the values
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)
            
            return left_sum + right_sum
        
        return dfs(root, 0)

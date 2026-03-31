# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def sum(node, count):
            
            if not node:
                return False
            
            
            count += node.val
            
            if not node.left and not node.right:
                return count == targetSum
            
            return sum(node.left, count) or sum(node.right, count)


        return sum(root, 0)
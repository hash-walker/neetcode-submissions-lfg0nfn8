# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            root = TreeNode(val)
            return root

        cur = root

        while cur:
            
            if cur.val < val and cur.right:
                    cur = cur.right
            elif cur.val > val and cur.left:
                    cur = cur.left
            else:
                if cur.val < val and not cur.right:
                    newNode = TreeNode(val)
                    cur.right = newNode
                    return root
                elif cur.val > val and not cur.left:
                    newNode = TreeNode(val)
                    cur.left = newNode
                    return root


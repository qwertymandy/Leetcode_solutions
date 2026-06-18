# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If one of the nodes is missing, return the existing subtree
        if not root1:
            return root2
        if not root2:
            return root1
        
        # Merge the values into root1 to save memory (destructive modification)
        root1.val += root2.val
        
        # Recursively merge the left and right children
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1

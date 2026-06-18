# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            # If a left child exists, we need to restructure it
            if curr.left:
                # Find the rightmost node in the left subtree (inorder predecessor or rightmost)
                rm = curr.left
                while rm.right:
                    rm= rm.right
                
                # Rewire the rightmost node's right to current's right subtree
                rm.right = curr.right
                
                # Move the entire left subtree to the right side
                curr.right = curr.left
                curr.left = None
                
            # Move on to the next node on the right path
            curr = curr.right

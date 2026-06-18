# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base cases
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
            
        # Use fast and slow pointers to find the middle element
        # 'prev' tracks the node right before the middle to disconnect the list
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Disconnect the left half from the middle node
        if prev:
            prev.next = None
            
        # Create the root node with the middle value
        root = TreeNode(slow.val)
        
        # Recursively build subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root



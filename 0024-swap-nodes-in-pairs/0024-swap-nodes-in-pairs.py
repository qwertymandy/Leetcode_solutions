class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to point to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' tracks the node right before the pair we want to swap
        prev = dummy
        
        # Ensure there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Identify the two nodes in the current pair
            first = prev.next
            second = prev.next.next
            
            # Change pointers to swap the pair
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move 'prev' two nodes ahead for the next iteration
            prev = first
            
        return dummy.next

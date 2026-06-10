class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0  # Pointer for the popped array
        
        for num in pushed:
            stack.append(num)  # Simulate push operation
            
            # Greedily pop elements as long as the top matches the next popped element
            while stack and stack[-1] == popped[i]:
                stack.pop()  # Simulate pop operation
                i += 1       # Move to the next expected popped element
                
        # If the simulation is valid, all elements should be successfully popped
        return not stack

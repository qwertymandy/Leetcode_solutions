from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)
        
        def backtrack(current_path):
            # Base case: if the path matches the length of nums, a valid permutation is formed
            if len(current_path) == len(nums):
                result.append(current_path.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue  # Skip elements that are already in the current permutation
                
                # Make choice
                visited[i] = True
                current_path.append(nums[i])
                
                # Recurse
                backtrack(current_path)
                
                # Undo choice (Backtrack)
                current_path.pop()
                visited[i] = False
                
        backtrack([])
        return result

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # Sorting helps with early pruning during the recursive search
        candidates.sort()
        
        def backtrack(index: int, current_combination: List[int], remaining_target: int):
            # Base Case: Successfully found a valid combination
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            # Explore candidates starting from the current index to avoid duplicate combinations
            for i in range(index, len(candidates)):
                # Pruning: If the candidate exceeds the remaining target, 
                # all subsequent candidates will also exceed it (since the list is sorted).
                if candidates[i] > remaining_target:
                    break
                
                # Step 1: Make a choice (include the candidate)
                current_combination.append(candidates[i])
                
                # Step 2: Explore recursively. Pass 'i' instead of 'i + 1' 
                # because we can reuse the same element multiple times.
                backtrack(i, current_combination, remaining_target - candidates[i])
                
                # Step 3: Backtrack (remove the choice)
                current_combination.pop()
                
        backtrack(0, [], target)
        return result

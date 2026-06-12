import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create hash sets to track seen digits for each structure
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells denoted by '.'
                if val == '.':
                    continue
                
                # Identify the specific 3x3 sub-box coordinate
                box_idx = (r // 3, c // 3)
                
                # Check for duplicates in row, column, or sub-box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Add the digit to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True

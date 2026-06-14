from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return an empty list if the input string is empty
        if not digits:
            return []
            
        # Map digits to their corresponding phone keypad letters
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, current_path: List[str]):
            # Base case: if the current combination matches the length of digits
            if len(current_path) == len(digits):
                res.append("".join(current_path))
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            possible_letters = digit_to_char[current_digit]
            
            # Explore all paths by picking one letter at a time
            for letter in possible_letters:
                current_path.append(letter)          # Choose
                backtrack(index + 1, current_path)   # Explore
                current_path.pop()                   # Unchoose (Backtrack)
                
        # Start backtracking from the first digit (index 0) with an empty path list
        backtrack(0, [])
        return res

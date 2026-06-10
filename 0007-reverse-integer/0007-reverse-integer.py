class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign and isolate the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Convert to string, reverse using slicing, and convert back to int
        reversed_num = int(str(x)[::-1]) * sign
        
        # Check for 32-bit signed integer overflow bounds
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
            
        return reversed_num

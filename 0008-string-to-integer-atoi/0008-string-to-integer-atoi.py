class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # 1. Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check for optional sign character
        sign = 1
        start_idx = 0
        if s[0] == '-':
            sign = -1
            start_idx = 1
        elif s[0] == '+':
            start_idx = 1
            
        # 3. Read and build the integer from numeric characters
        res = 0
        for i in range(start_idx, len(s)):
            if not s[i].isdigit():
                break
            res = res * 10 + int(s[i])
            
            # Early clamping check to prevent unnecessary large values
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
                
        # 4. Apply final sign and return bounded result
        res = sign * res
        return max(INT_MIN, min(INT_MAX, res))

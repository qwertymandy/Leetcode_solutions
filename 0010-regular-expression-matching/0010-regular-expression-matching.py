from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            # Base Case: If we reach the end of the pattern, 
            # the string must also be completely consumed.
            if j == n:
                return i == m
            
            # Check if the current characters match
            current_match = i < m and (s[i] == p[j] or p[j] == '.')
            
            # If the next character in pattern is '*'
            if j + 1 < n and p[j + 1] == '*':
                # Option 1: Skip the '*' and its preceding element (match 0 times)
                # Option 2: Consume current char from s if it matches, and stay on the same pattern character
                return dfs(i, j + 2) or (current_match and dfs(i + 1, j))
            
            # If there is no '*', move both pointers forward if current matches
            return current_match and dfs(i + 1, j + 1)
            
        return dfs(0, 0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns starting with '*' that can match an empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                break
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: Characters match or pattern has '?'
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # Case 2: Pattern has '*'
                elif p[j - 1] == '*':
                    # dp[i][j-1]: '*' matches 0 characters
                    # dp[i-1][j]: '*' matches 1 or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    
        return dp[m][n]

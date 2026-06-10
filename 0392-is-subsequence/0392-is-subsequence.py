class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_iterator = iter(t)
        return all(char in t_iterator for char in s)

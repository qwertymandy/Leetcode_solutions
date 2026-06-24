import math
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g=numsDivide[0]
        for x in numsDivide[1:]:
            g=math.gcd(g,x)

        nums.sort()
        for i, num in enumerate(nums):
            if g%num==0:
                return i
            
        return -1



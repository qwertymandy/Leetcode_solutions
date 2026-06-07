class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a slow pointer to track where the next valid element goes
        k = 0
        
        for num in nums:
            # If we have placed fewer than 2 elements, or the current number
            # is different from the element placed 2 steps behind, it's valid.
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1
                
        return k

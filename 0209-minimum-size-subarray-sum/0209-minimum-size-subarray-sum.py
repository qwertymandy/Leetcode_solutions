class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the left pointer, running sum, and minimum length
        left = 0
        current_sum = 0
        min_len = float('inf')
        
        # Iterate through the array using the right pointer
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left as long as the sum satisfies the target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        # If min_len was updated, return it; otherwise, no valid subarray exists
        return min_len if min_len != float('inf') else 0

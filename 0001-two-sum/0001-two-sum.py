class Solution:
    def twoSum(self, nums, target):
        # This dictionary acts as our HashMap
        # Key: the number, Value: its index
        seen_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen_map:
                return [seen_map[complement], i]
            
            # Store the current number and its index
            seen_map[nums[i]] = i

        return []

# For local testing - create an instance first
sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(f"Optimized result: {sol.twoSum(nums, target)}")
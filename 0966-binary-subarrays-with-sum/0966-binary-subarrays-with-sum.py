from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_count = defaultdict(int)
        sum_count[0] = 1  # To handle the case where a subarray itself equals the goal
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            
            # Check if there's a prefix_sum that makes the subarray sum equal to goal
            if prefix_sum - goal in sum_count:
                count += sum_count[prefix_sum - goal]
            
            # Store the current prefix_sum count
            sum_count[prefix_sum] += 1
        
        return count

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect cycle
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]  # Move slow by 1 step
            fast = nums[nums[fast]]  # Move fast by 2 steps
            if slow == fast:  # Cycle detected
                break

        # Phase 2: Find the duplicate number
        slow = nums[0]  # Reset slow to start
        while slow != fast:
            slow = nums[slow]  # Move both by 1 step
            fast = nums[fast]
        
        return slow  # Found the duplicate

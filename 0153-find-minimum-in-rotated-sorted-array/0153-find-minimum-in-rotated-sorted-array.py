class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for i in range(len(nums)):
            if mini > nums[i]:
                mini = nums[i]
        return mini
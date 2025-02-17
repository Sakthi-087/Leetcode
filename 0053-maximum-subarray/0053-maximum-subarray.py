class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < curr_sum+nums[i]:
                curr_sum = curr_sum+nums[i]
            else:
                curr_sum = nums[i]
            if max_sum < curr_sum:
                max_sum = curr_sum
        return max_sum
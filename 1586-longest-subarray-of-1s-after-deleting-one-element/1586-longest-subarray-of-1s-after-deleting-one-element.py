class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length, left, zero_count = 0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            while zero_count > 1:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            if max_length < right-left:
                max_length = right-left
        return max_length
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                count+=1
        return count
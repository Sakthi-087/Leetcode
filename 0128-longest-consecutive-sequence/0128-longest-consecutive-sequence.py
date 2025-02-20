class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        tempCount = 1

        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                tempCount+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                tempCount = 1
            if tempCount > count:
                    count = tempCount
        if tempCount > count:
            count = tempCount
        return count
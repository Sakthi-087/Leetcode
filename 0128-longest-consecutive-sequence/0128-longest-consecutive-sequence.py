class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        tempCount = 1

        if len(nums)==1:
            return tempCount

        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                tempCount+=1
            elif nums[i-1] == nums[i] and len(nums) > 3:
                continue
            else:
                tempCount = 1
            if tempCount > count:
                    count = tempCount
            print(tempCount,end="  ")
            print(count)
        return count
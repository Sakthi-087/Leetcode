class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li = []
        count = 0
        for i in nums:
            count = 0
            for j in nums:
                if i>j:
                    count+=1
            li.append(count)
        return li
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = []
        for i in range(len(nums)):
            if nums[i]==target:
                li.append(i)
                break

        if not li:
            return [-1,-1]

        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                li.append(j)
                break

        return li
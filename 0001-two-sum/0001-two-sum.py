class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for p1, num in enumerate(nums):
            rem = target - num
            if rem in hashmap:
                return [hashmap[rem],p1]
            hashmap[num] = p1
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        prefix_sum=0
        for n in nums:
            prefix_sum+=n
            count+=prefix_count[prefix_sum-goal]
            prefix_count[prefix_sum]+=1
        return count
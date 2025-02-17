from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for num in nums:
            pre_sum+=num
            if (pre_sum-k) in prefix_sums:
                count+=prefix_sums[pre_sum-k]
            prefix_sums[pre_sum]+=1
        return count
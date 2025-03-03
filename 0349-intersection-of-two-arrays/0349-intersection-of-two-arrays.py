class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        t = set(nums2)
        a = s.intersection(t)
        return list(a)
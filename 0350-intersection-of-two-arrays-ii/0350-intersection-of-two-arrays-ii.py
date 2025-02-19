class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:  
                    li.append(nums1[i])
                    nums2[j] = float('inf')  # Mark as used to avoid duplicate counts
                    break
        return li

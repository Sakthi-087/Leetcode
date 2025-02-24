class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # If needle is empty, return 0 as per the problem statement
        if m == 0:
            return 0
        
        # Slide through the haystack with window size of len(needle)
        for i in range(n - m + 1):
            # Check substring manually
            if haystack[i:i+m] == needle:
                return i
        
        # If no match found
        return -1

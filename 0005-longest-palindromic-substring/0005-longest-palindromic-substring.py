class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCentre(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        maxStr=''
        for i in range(len(s)):
            odd_palindrome = expandAroundCentre(i,i)
            even_palindrome = expandAroundCentre(i,i+1)
            maxStr = max(maxStr, odd_palindrome, even_palindrome, key=len)
        return maxStr
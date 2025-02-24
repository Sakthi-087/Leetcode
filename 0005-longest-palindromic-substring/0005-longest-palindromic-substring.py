class Solution:
    def longestPalindrome(self, s: str) -> str:
        newStr = ""
        maxStr = ""
        for i in range(len(s)):
            newStr = ""
            for j in range(i,len(s)):
                newStr += s[j]
                if newStr == newStr[::-1] and len(maxStr) < len(newStr):
                    maxStr = newStr
                    print(maxStr)
        return maxStr
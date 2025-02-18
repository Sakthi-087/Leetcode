class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for i in s:
            i = i.lower()
            if i.isalnum():
                newStr+=i
        return newStr==newStr[::-1]
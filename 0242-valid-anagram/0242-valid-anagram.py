class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        setT = set(t)
        for i in setT:
            if s.count(i) < t.count(i):
                return False
        return True
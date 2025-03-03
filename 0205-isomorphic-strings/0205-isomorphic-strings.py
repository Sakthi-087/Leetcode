class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_map = {}
        rev_map = {}
        for i in range(len(s)):
            if s[i] in iso_map:
                if iso_map[s[i]] != t[i]:
                    return False
            else:
                iso_map[s[i]] = t[i]
            
            if t[i] in rev_map:
                if rev_map[t[i]] != s[i]:
                    return False
            else:
                rev_map[t[i]] = s[i]
        return True
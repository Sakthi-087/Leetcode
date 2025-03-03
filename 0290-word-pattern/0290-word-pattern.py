class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        
        if len(pattern) != len(word):
            return False
        
        word_map = {}
        rev_map = {}
        for i in range(len(pattern)):
            print(rev_map)
            if pattern[i] in word_map:
                if word_map[pattern[i]] != word[i]:
                    return False
            else:
                word_map[pattern[i]] = word[i]
            
            if word[i] in rev_map:
                if rev_map[word[i]] != pattern[i]:
                    return False
            else:
                rev_map[word[i]] = pattern[i]
        return True
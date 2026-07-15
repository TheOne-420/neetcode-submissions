class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        h1 = {}
        h2 = {}
        for ch in s:
            h1[ch] = 1 + h1.get(ch, 0)
        for ch in t:
            h2[ch] = 1 + h2.get(ch, 0)
        
        return h1 == h2
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}

        for c in s:
            hashS[c] = 1 + hashS.get(c, 0)
        
        hashT = {}

        for c in t:
            hashT[c] = 1 + hashT.get(c, 0)
        
        return hashS == hashT
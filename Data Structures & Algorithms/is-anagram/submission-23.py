class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
        
        for i in range(len(t)):
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        
        return hashS == hashT
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        s = list(s)

        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
        
        for char in t:
            if char in hashMap:
                hashMap[char] -= 1
            elif char not in hashMap:
                return False
        
        for value in hashMap.values():
            if value != 0:
                return False 
        return True

        
        
             
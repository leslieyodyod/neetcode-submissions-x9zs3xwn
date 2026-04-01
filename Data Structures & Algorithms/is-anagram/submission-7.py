
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict()

        if len(s) != len(t):
            return False 
            
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        
        for c in t:
            if c in hashMap and hashMap[c] > 0:
                hashMap[c] -= 1
            else:
                return False
        
        return True
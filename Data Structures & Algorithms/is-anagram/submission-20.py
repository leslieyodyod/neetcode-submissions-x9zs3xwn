class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}

        if len(t) != len(s):
            return False

        for char in s:
            if char in hashS:
                hashS[char] += 1
            else:
                hashS[char] = 1
        
        for char in t:
            if char in hashS:
                hashS[char] -= 1
            else:
                return False
        
        for char, total in hashS.items():
            if total != 0:
                return False
        return True
        


        
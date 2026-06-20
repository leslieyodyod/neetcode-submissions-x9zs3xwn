class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        hashMap = {}

        for char in s:
            hashMap[char] = ord(char)

        for i in range(len(s) - 1):
            diff = abs(hashMap.get(s[i]) - hashMap.get(s[i + 1]))
            res += diff
        return res

        
    

        
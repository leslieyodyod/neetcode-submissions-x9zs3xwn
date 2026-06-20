class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        l, r = 0, 1

        hashMap = {}

        for char in s:
            hashMap[char] = ord(char)

        while l < r and r < len(s):
            res += abs(hashMap.get(s[l]) - hashMap.get(s[r]))
            l += 1
            r += 1
        return res

    

        
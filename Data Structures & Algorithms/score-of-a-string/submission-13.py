class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0


        l, r = 0, 1

        while l < r and r < len(s):
            diff = abs(ord(s[l]) - ord(s[r]))
            res += diff
            l += 1
            r += 1
        return res

        
    

        
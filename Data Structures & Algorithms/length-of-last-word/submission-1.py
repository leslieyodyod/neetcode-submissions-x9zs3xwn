class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1

        while r > 0 and s[r] == " ":
            r -= 1
        l = r

        while l > 0 and s[l] != " ":
            l -= 1
        
        return len(s) if len(s) < 2 else len(s[l + 1: r + 1])
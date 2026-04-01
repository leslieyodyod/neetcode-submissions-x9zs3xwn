class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == " ":
                l += 1
            elif s[r] == " ":
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
                
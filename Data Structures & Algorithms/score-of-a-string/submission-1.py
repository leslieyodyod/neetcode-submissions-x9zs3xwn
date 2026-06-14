class Solution:
    def scoreOfString(self, s: str) -> int:
        #create a dictionary mapping asci values to letters in s 
        #iterate through s with left and right pointers
        #calculate the difference, then keep moving through s
        #each difference gets added to res 
        #return res 
        l, r = 0, 1
        res = 0
        while l < r and r < len(s):
            diff = abs(ord(s[l]) - ord(s[r]))
            res += diff 
            l += 1
            r += 1
        return res 
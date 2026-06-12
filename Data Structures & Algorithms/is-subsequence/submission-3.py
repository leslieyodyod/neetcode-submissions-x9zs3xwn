class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #use two pointers
        #both pointers start at beginning of each string
        #iterate through second string until characters match
        #if you get to the end of the string and they don't
        #return false 
        ptr1, ptr2 = 0, 0 

        while ptr1 < len(s) and ptr2 < len(t):
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
            ptr2 += 1
        return ptr1 == len(s)



                

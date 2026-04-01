class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create freq map for s
        s_freq = dict()
        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1

        #second freq map
        t_freq = dict()
        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1
        
        #compare
        return s_freq == t_freq

            
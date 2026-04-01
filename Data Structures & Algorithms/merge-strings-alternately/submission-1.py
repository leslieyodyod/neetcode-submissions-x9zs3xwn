class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        word1 = list(word1)
        word2 = list(word2)
        res = []

        while p1 < len(word1) and p2 < len(word2):
            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1
    
        
        if len(word2) > len(word1):
            for char in word2[p2:]:
                res.append(char)
        elif len(word2) < len(word1):
            for char in word1[p1:]:
                res.append(char)
        
        return "".join(res)
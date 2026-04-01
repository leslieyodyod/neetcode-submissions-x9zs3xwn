from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        hashMap = defaultdict(set)
        minLen = min(strs, key=len)

        for string in strs:
            for i in range(len(minLen)):
                hashMap[i].add(string[i])
            
        for value in hashMap.values():
            for item in value:
                if len(value) != 1:
                    return "".join(res)
                res.append(item)
            

        
        return "".join(res)

            
        
        
        
        

        



        
        




        

            
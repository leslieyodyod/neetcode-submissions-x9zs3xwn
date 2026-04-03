class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort strings by length 
        strs = sorted(strs, key=len)

        #shortest word becomes prefix 
        prefix = strs[0]
        
        #compare characters until they don't match 
        for i in range(1,len(strs)):
            ptr = 0
            while ptr < len(prefix):
                if strs[i][ptr] != prefix[ptr]:
                    prefix = prefix[:ptr]
                ptr += 1
        return prefix 
                

        


        

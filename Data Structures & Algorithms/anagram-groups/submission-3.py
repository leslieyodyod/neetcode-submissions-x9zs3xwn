class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        groups = {}

        for word in strs:
            sort = "".join(sorted(word))
            if sort in groups:
                groups[sort].append(word)
            else:
                groups[sort] = [word]
        
        return list(groups.values())

        


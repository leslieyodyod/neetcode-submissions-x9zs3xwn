from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        res = []

        for string in strs:
            sortedstr = "".join(sorted(string))
            seen[sortedstr].append(string)
        
        for value in seen.values():
            res.append(value)
        
        return res
           
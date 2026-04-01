from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        seen = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in seen:
                seen[sorted_string] = [string]
            else:
                seen[sorted_string].append(string)
        
        for item in seen:
            res.append(seen[item])
         
        return res
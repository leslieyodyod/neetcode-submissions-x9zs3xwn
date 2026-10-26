class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))
            hashStr[s_sorted].append(s)
        
        return [x for x in hashStr.values()]
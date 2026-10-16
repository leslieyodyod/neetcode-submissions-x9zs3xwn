class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = defaultdict(list)
        res = []
        for s in strs:
            sortS = "".join(sorted(s))
            hashStr[sortS].append(s)
        for val in hashStr.values():
            res.append(val)
        return res
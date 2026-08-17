class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashRes = collections.defaultdict(list)
        res = []
        for s in strs:
            s_sorted = "".join(sorted(s))
            hashRes[s_sorted].append(s)
        
        for val in hashRes.values():
            res.append(val)

        return res

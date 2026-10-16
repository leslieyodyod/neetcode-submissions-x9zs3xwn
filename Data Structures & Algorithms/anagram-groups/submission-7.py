class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = defaultdict(list)

        for s in strs:
            sortS = "".join(sorted(s))
            hashStr[sortS].append(s)
        return [val for val in hashStr.values()]
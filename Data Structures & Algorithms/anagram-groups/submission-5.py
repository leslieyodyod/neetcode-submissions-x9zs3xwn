class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = {}

        for st in strs:
            sortedSt = "".join(sorted(st))
            if sortedSt in hashStr:
                hashStr[sortedSt].append(st)
            else:
                hashStr[sortedSt] = [st]

        return [value for value in hashStr.values()]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        res = []

        for j in range(len(shortest)):
            for st in strs:
                if st[j] != shortest[j]:
                    return "".join(res)
            res.append(shortest[j])
        return "".join(res)

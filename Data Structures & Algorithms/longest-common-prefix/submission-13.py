from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        hashStr = defaultdict(list)

        for string in strs:
            for i in range(len(shortest)):
                hashStr[i].append(string[i])

        stack = []

        for idx, chars in hashStr.items():
            seen = set(chars)
            if len(seen) == 1:
                stack.append(chars[0])
            else:
                break
        return "".join(stack)

        
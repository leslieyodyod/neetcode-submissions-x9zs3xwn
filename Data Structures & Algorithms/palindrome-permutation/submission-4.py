class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashStr = {}

        for char in s:
            if char not in hashStr:
                hashStr[char] = 1
            else:
                hashStr[char] += 1

        oddCount = 0

        for char in hashStr:
            if hashStr.get(char) % 2 != 0:
                oddCount += 1
        return oddCount <= 1
                
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res = 0

        hashKey = {}

        for i in range(len(keyboard)):
            hashKey[keyboard[i]] = i

        prev = 0

        for char in word:
            res += abs(prev - hashKey[char])

            prev = hashKey[char]
        
        return res

        

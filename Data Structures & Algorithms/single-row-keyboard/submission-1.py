class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res = abs(0 - keyboard.index(word[0]))
           
        for i in range(len(word) - 1):
            diff = abs(keyboard.index(word[i]) - keyboard.index(word[i + 1]))
            res += diff
        return res